import socket
import time
import random

from Player import Player
from Shop import ShopContents
from assets.modules.elements.constructs.troops.Troop import Troop
from Maps import *

from assets.modules.elements.environment.MineralPile import MineralPile

class StuftCraftServer:
    def __init__(self):
        self.Map: Map
        self.elements = []
        self.socket = socket.socket()
        self.connections = []
        self.port = 4001

        self.running = True

    def run(self, player_count, map: Map):
        self.socket.bind((socket.gethostname(), self.port))
        self.socket.listen(player_count)
        print(self.socket.getsockname())

        self.Map = map
        for p in range(player_count):
            connection, stuff = self.socket.accept()
            player_name = connection.recv(1024, 0).decode("utf8")
            print(f"{player_name} just joined")
            player = Player(player_name, p, self.Map.get_home(p), 0)
            connection.send(self.map_to_message(player) + self.state_to_message(player), 0)
            self.connections.append((connection, player))

        self.elements = self.Map.get_elements(list(p for c, p in self.connections))

        while self.running:
            dead = []
            for e in self.elements[:]:
                if e.alive:
                    e.update(self.elements)
                    if e.position[0] > self.Map.size[0]:
                        e.position[0] = self.Map.size[0]
                    elif e.position[0] < 0:
                        e.position[0] = 0
                    if e.position[1] > self.Map.size[1]:
                        e.position[1] = self.Map.size[1]
                    elif e.position[1] < 0:
                        e.position[1] = 0
                else:
                    dead.append(e)
            for e in dead:
                self.elements.remove(e)

            for con, player in self.connections[:]:
                message = con.recv(1024, 0)
                while len(message) > 0:
                    mes, message = message[0:16], message[16:]
                    if mes == b"fullstateupdate;":
                        con.send(self.state_to_message(player), 0)
                    elif mes[0:4] == b"buy:":
                        id = int.from_bytes(mes[4:8], "little")
                        x = int.from_bytes(mes[8:12], "little")
                        y = int.from_bytes(mes[12:16], "little")

                        self.purchase(player, id, [x,y])
                    elif mes[0:4] == b"slct":
                        radius = int.from_bytes(mes[4:8], "little")
                        x = int.from_bytes(mes[8:12], "little")
                        y = int.from_bytes(mes[12:16], "little")
                        player.selected = []
                        for e in self.elements:
                            if isinstance(e, Troop) and e.player is player:
                                if ((e.position[0] - x) ** 2 + (e.position[1] - y) ** 2) < radius ** 2:
                                    player.selected.append(e)

                    elif mes[0:4] == b"move":
                        radius = int.from_bytes(mes[4:8], "little")
                        x = int.from_bytes(mes[8:12], "little")
                        y = int.from_bytes(mes[12:16], "little")
                        for e in player.selected:
                            e.mode = e.TRAVELING
                            xerror = random.randint(-radius, radius)
                            yradius = int((radius ** 2 - xerror ** 2) ** .5)
                            yerror = random.randint(-yradius, yradius)
                            e.destination = [x + xerror, y + yerror]

                    elif mes == b"exitcode\0\0\0\0\0\0\0\0":
                        con.close()
                        self.connections.remove((con, player))
                        if len(self.connections) == 0:
                            self.running = False
                    elif mes == b"new\0\0\0\0\0\0\0\0\0\0\0\0\0":
                        con.send(self.state_to_message(player), 0)

            time.sleep(0.1 - (time.time_ns() % 100000000) / 1000000000)

        for c in self.connections:
            c[0].close()

        self.socket.close()

    def purchase(self, player, id, pos):
        if ShopContents[id]["Class"].place_condition(player, pos, self.elements):
            if player.minerals >= ShopContents[id]["Cost"]:
                self.elements.append(ShopContents[id]["Class"](player, pos))
                player.minerals -= ShopContents[id]["Cost"]

    def state_to_message(self, player: Player):
        message = b"full"

        if player.command_centers > 0:
            if len(list(p.command_centers for c, p in self.connections if p.command_centers > 0)) > 1:
                status = 2
            else:
                status = 1
        else:
            status = 0

        message += status.to_bytes(4, "little")

        message += player.minerals.to_bytes(4, "little")

        #TODO This should be done once for all players
        # (unless each player will want it at a different time)
        for e in self.elements:
            ele = b""
            ele += e.get_texture().to_bytes(4, "little")
            ele += e.draw_position()[0].to_bytes(4, "little")
            ele += e.draw_position()[1].to_bytes(4, "little")
            message += ele

        return message

    def map_to_message(self, player: Player):
        return (self.Map.size[0].to_bytes(4, "little") +
                self.Map.size[1].to_bytes(4, "little") +
                player.home[0].to_bytes(4, "little") +
                player.home[1].to_bytes(4, "little")
                )

if __name__ == "__main__":
    client = StuftCraftServer()
    client.run(2, PlainMap)
