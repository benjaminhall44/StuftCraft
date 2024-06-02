import socket
import time
import threading

from Element import Element
from Vector import Vector
from Messenger import Messenger

class StuftCraftServer:
    messenger: Messenger
    def __init__(self):
        self.elements = []
        self.elements.append(Element())
        self.socket = socket.socket()
        self.connections = []
        self.port = 4001

        self.running = True

    def run(self, player_count):
        self.socket.bind((socket.gethostname(), self.port))
        self.socket.listen(player_count)

        print(self.socket.getsockname())
        for p in range(player_count):
            connection, stuff = self.socket.accept()
            player = connection.recv(1024, 0).decode("utf8")
            self.connections.append((connection, player))

        while self.running:
            for e in self.elements:
                e.update()

            for con, player in self.connections[:]:
                message = con.recv(1024, 0)
                for mes in message.split(b";"):
                    if mes == b"exit":
                        con.close()
                        self.connections.remove((con, player))
                        if len(self.connections) == 0:
                            self.running = False
                    elif mes == b"spawn":
                        if player == "player1":
                            self.elements.append(Element())
                        else:
                            self.elements = []
                    elif mes == b"new":
                        con.send(self.state_to_message(), 0)
                    elif mes == b"full":
                        con.send(self.state_to_message(), 0)

            time.sleep(0.1 - (time.time_ns() % 100000000) / 1000000000)

        for c in self.connections:
            c[0].close()

        self.socket.close()

    def state_to_message(self):
        message = b"full"
        for e in self.elements:
            ele = b""
            ele += e.get_id().to_bytes(4, "little")
            ele += e.draw_position().x.to_bytes(4, "little")
            ele += e.draw_position().y.to_bytes(4, "little")
            message += ele

        return message


if __name__ == "__main__":
    client = StuftCraftServer()
    client.run(2)
