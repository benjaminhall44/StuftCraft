import socket
import sys
import time
import random

from assets.modules.components.Player import Player
from assets.modules.libraries.Shop import ShopContents
from assets.modules.elements.constructs.troops.Troop import Troop
from assets.modules.elements.constructs.worker.Worker import Worker
from assets.modules.elements.constructs.machine.CarMachine import CarMachine
from assets.modules.libraries.Maps import *


class StuftCraftServer:
    def __init__(self, player_count: int, map: str, port=4001):
        self.elements = []
        self.socket = socket.socket()
        self.connections = []
        self.port = port
        self.socket.bind((socket.gethostname(), self.port))
        self.socket.settimeout(0.1)

        self.running = True

        self.Map: Map = Maps[map][player_count]
        self.player_count = player_count

        self.connecting = True

    def get_address(self):
        address = self.socket.getsockname()
        return f"{address[0]}:{address[1]}"

    def run(self):
        self.socket.listen(self.player_count)

        for p in range(self.player_count):
            trying = True
            while trying:
                try:
                    connection, stuff = self.socket.accept()
                    connection.settimeout(0.01)
                    player_name = connection.recv(1024, 0).decode("utf8")
                    print(f"{player_name} just joined")
                    player = Player(player_name, p, self.Map.get_home(p), 0)
                    connection.send(self.map_to_message(player) + self.state_to_message(player), 0)
                    self.connections.append((connection, player))
                    trying = False
                except:
                    for con, player in self.connections[:]:
                        message = self.get_message(con)
                        while len(message) > 0:
                            mes, message = message[0:16], message[16:]
                            c = mes[0:4]
                            if c == b"full":
                                con.send(self.state_to_message(player), 0)
                            elif c == b"exit":
                                print(f"{player.name} just quit")
                                con.close()
                                self.connections.remove((con, player))
                                if len(self.connections) == 0:
                                    print("All players have quit: shutting down")
                                    self.running = False
                                    self.socket.close()
                                    return

        self.elements = self.Map.get_elements(list(p for c, p in self.connections))
        self.connecting = False

        while self.running:
            st_time = time.time_ns() + 100000000
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
                message = self.get_message(con)
                while len(message) > 0:
                    mes, message = message[0:16], message[16:]
                    c = mes[0:4]
                    v = int.from_bytes(mes[4:8], "little")
                    x = int.from_bytes(mes[8:12], "little")
                    y = int.from_bytes(mes[12:16], "little")

                    if c == b"full":
                        con.send(self.state_to_message(player), 0)
                    elif c == b"buy:":
                        self.purchase(player, v, [x,y])
                    elif c == b"strp":
                        player.selected = []
                        for e in self.elements:
                            if (isinstance(e, Troop) or isinstance(e, CarMachine)) and e.player is player:
                                if ((e.position[0] - x) ** 2 + (e.position[1] - y) ** 2) < v ** 2:
                                    player.selected.append(e)

                    elif c == b"swrk":
                        player.selected = []
                        for e in self.elements:
                            if isinstance(e, Worker) and e.player is player:
                                if ((e.position[0] - x) ** 2 + (e.position[1] - y) ** 2) < v ** 2:
                                    player.selected.append(e)

                    elif c == b"move":
                        for e in player.selected:
                            e.set_destination([x,y], v, self.elements)

                    elif c == b"exit":
                        print(f"{player.name} just quit")
                        con.close()
                        self.connections.remove((con, player))
                        if len(self.connections) == 0:
                            print("All players have quit: shutting down")
                            self.running = False
            time.sleep(max(st_time - time.time_ns(), 0) / 1000000000)

        for c in self.connections:
            c[0].close()

        self.socket.close()

    @staticmethod
    def get_message(con) -> bytes:
        try:
            return con.recv(1024, 0)
        except TimeoutError:
            return b""

    def purchase(self, player, id, pos):
        if ShopContents[id]["Class"].place_condition(player, pos, self.elements):
            if player.minerals >= ShopContents[id]["Cost"]:
                constr = ShopContents[id]["Class"](player, pos)
                if isinstance(constr, Troop):
                    constr.mode = Troop.TRAVELING
                    xerror = random.randint(-50, 50)
                    yradius = int((50 ** 2 - xerror ** 2) ** .5)
                    yerror = random.randint(-yradius, yradius)
                    constr.destination = [pos[0] + xerror, pos[1] + yerror]
                self.elements.append(constr)
                player.minerals -= ShopContents[id]["Cost"]

    def state_to_message(self, player: Player):
        message = b"full"

        if self.connecting:
            status = 3
        else:
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
                self.Map.color[0].to_bytes(4, "little") +
                self.Map.color[1].to_bytes(4, "little") +
                self.Map.color[2].to_bytes(4, "little") +
                player.home[0].to_bytes(4, "little") +
                player.home[1].to_bytes(4, "little")
                )

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        player_count = int(sys.argv[1])
        map = sys.argv[2]
        port = int(sys.argv[3])
    else:
        player_count = 2
        map = "Plain"
        port = 4001
    server = StuftCraftServer(player_count, map, port)
    print(f"Running on: {server.get_address()}")
    server.run()
