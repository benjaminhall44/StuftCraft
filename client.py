import pygame
import socket
import time

from Sprite import Sprite
from Vector import Vector
from Messenger import Messenger

class StuftCraftClient:
    messenger: Messenger

    def __init__(self):
        self.screen = pygame.display.set_mode(size=[1000, 700], flags=pygame.RESIZABLE)
        self.menu = None
        self.view = Vector()

        # status #

        self.elements = []

        self.socket = socket.socket()

        self.address = None

    def connect(self, address):
        self.address = address

    def play(self):
        self.connect_to_server()
        self.animate()

        MouseDown = False
        MousePosition = [0,0]
        PreviousMousePosition = [0,0]

        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    MouseDown = True
                    self.socket.send(b"spawn;", 0)
                elif event.type == pygame.MOUSEBUTTONUP:
                    MouseDown = False
                elif event.type == pygame.MOUSEMOTION:
                    MousePosition = Vector(event.pos)
                    if MouseDown:
                        self.view = self.view - (MousePosition - PreviousMousePosition)
                    PreviousMousePosition = Vector(event.pos)

            self.update()
            self.animate()

    def animate(self):
        size = self.screen.get_size()

        self.screen.fill([0,255,0])

        for s in self.elements:
            s.draw(self.screen, self.view)

        self.draw_menu()

        pygame.display.flip()

    def draw_menu(self):
        pass

    def exit(self):
        playing = False
        self.socket.send(b"exit;", 0)
        self.socket.close()
        pygame.quit()

    def connect_to_server(self):
        if self.address is None:
            raise Exception("No address provided")
        self.socket.connect(self.address)
        player_name = input("Enter Name: ")
        self.socket.send(player_name.encode("utf8"), 0)

        self.update()

    def update(self):
        self.socket.send(b"full;", 0)
        mes = self.socket.recv(1024 * 1024, 0)
        self.state_from_message(mes)

    def state_from_message(self, message: bytes):
        message = message[4:]
        self.elements = []
        for s in range(len(message) // 12):
            p = message[s * 12 : s * 12 + 12]
            id = int.from_bytes(p[0:4], "little")
            x = int.from_bytes(p[4:8], "little")
            y = int.from_bytes(p[8:12], "little")

            ele = Sprite(id, x, y)
            self.elements.append(ele)


if __name__ == "__main__":
    client = StuftCraftClient()
    ipAddress = '192.168.1.117'
    port = 4001
    address = (ipAddress, port)
    client.connect(address)
    client.play()
