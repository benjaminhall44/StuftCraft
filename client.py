import time

import pygame
import socket
import sys

from assets.modules.components.Sprite import Sprite
from assets.modules.components.Menu import Menu

class StuftCraftClient:
    Textures = [
        pygame.image.load("assets/graphics/menu/icons/buildings/base.png"),

        pygame.image.load("assets/graphics/menu/icons/troops/three.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/four.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/man.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/lasereagle.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/bigman.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/spider.png"),
        pygame.image.load("assets/graphics/menu/icons/troops/flyingtank.png"),

        pygame.image.load("assets/graphics/menu/icons/workers/miner.png"),

        pygame.image.load("assets/graphics/menu/icons/machines/car.png"),

        pygame.image.load("assets/graphics/menu/icons/research/dragon.png")
    ]

    def __init__(self, player_name: str):
        self.screen = pygame.display.set_mode(size=[1000, 700], flags=pygame.RESIZABLE)
        pygame.display.set_caption("Stuft Craft")
        pygame.display.set_icon(pygame.image.load("assets/graphics/menu/icon.png"))
        self.menu = Menu()
        self.home = [0, 0]
        self.view = [0, 0]
        self.MapSize = [100,100]
        self.MapColor = (255, 255, 255)
        # status #

        self.player_name = player_name
        self.layers: list[list[Sprite]]
        self.minerals = 0

        self.status = 2

        self.socket = socket.socket()

        self.address = None

        self.MouseDown = False
        self.scrolling = False
        self.MousePosition = [0, 0]
        self.PreviousMousePosition = [0, 0]

        self.buying = None

        self.selecting = False
        self.selection_radius = 100
        self.targeting = False

    def connect(self, address):
        self.address = address
        self.connect_to_server()

    def play(self):
        self.animate()
        UpDown = False
        DownDown = False
        LeftDown = False
        RightDown = False
        ShiftDown = False

        self.playing = True
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        UpDown = True
                    elif event.key == pygame.K_DOWN:
                        DownDown = True
                    elif event.key == pygame.K_LEFT:
                        LeftDown = True
                    elif event.key == pygame.K_RIGHT:
                        RightDown = True
                    elif event.key == pygame.K_LSHIFT:
                        ShiftDown = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        UpDown = False
                    elif event.key == pygame.K_DOWN:
                        DownDown = False
                    elif event.key == pygame.K_LEFT:
                        LeftDown = False
                    elif event.key == pygame.K_RIGHT:
                        RightDown = False
                    elif event.key == pygame.K_LSHIFT:
                        ShiftDown = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.status == 2:
                            self.MouseDown = True
                            size = self.screen.get_size()
                            if size[0] - 210 < event.pos[0] < size[0] - 10 and 10 < event.pos[1] < 210:
                                self.click_minimap(event.pos)
                            elif size[0] - 40 < event.pos[0] < size[0] - 10 and 215 < event.pos[1] < 245:
                                self.view = self.home[:]
                            else:
                                result, value = self.menu.click_menu(size, event.pos)
                                if result == Menu.BOUGHT:
                                    if self.buying is None or self.buying != value:
                                        self.buying = value
                                    else:
                                        self.buying = None
                                elif result == Menu.MISSED_MENU:
                                    if self.buying is not None:
                                        self.message(b"buy:", self.buying, self.view[0] + self.MousePosition[0], self.view[1] + self.MousePosition[1])
                                        if not ShiftDown:
                                            self.buying = None
                                    elif self.selecting and self.menu.control_mode == self.menu.TROOPCONTROL:
                                        self.message(b"strp", self.selection_radius,
                                                     self.view[0] + self.MousePosition[0],
                                                     self.view[1] + self.MousePosition[1])
                                        self.selecting = False
                                        self.targeting = True
                                    elif self.selecting and self.menu.control_mode == self.menu.WORKERCONTROL:
                                        self.message(b"swrk", self.selection_radius,
                                                     self.view[0] + self.MousePosition[0],
                                                     self.view[1] + self.MousePosition[1])
                                        self.selecting = False
                                        self.targeting = True
                                    elif self.targeting:
                                        self.message(b"move", self.selection_radius, self.view[0] + self.MousePosition[0], self.view[1] + self.MousePosition[1])
                                        self.targeting = False
                                elif result == Menu.SCROLL or result == Menu.SCROLL_TAB:
                                    self.scrolling = True
                                elif result == Menu.CONTROL:
                                    if not self.selecting:
                                        self.selecting = True
                                    else:
                                        self.selecting = False
                                        self.targeting = False
                                elif result == Menu.CONTROL_RADIUS_UP:
                                    self.selection_radius += 10
                                elif result == Menu.CONTROL_RADIUS_DOWN:
                                    self.selection_radius -= 10
                                    if self.selection_radius < 10:
                                        self.selection_radius = 10

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.MouseDown = False
                elif event.type == pygame.MOUSEMOTION:
                    self.MousePosition = event.pos
                    if self.MouseDown:
                        if self.screen.get_size()[0] - 210 < event.pos[0] < self.screen.get_size()[0] - 10 and 10 < event.pos[1] < 210:
                            self.click_minimap(event.pos)
            if self.scrolling and self.MouseDown:
                result, value = self.menu.click_menu(self.screen.get_size(), self.MousePosition)
                if result != Menu.SCROLL and result != Menu.SCROLL_TAB:
                    self.scrolling = False
            if UpDown:
                self.view[1] -= 10
                if self.view[1] < 0:
                    self.view[1] = 0
            if DownDown:
                self.view[1] += 10
            if self.view[1] > self.MapSize[1] - self.screen.get_size()[1]:
                self.view[1] = self.MapSize[1] - self.screen.get_size()[1]
            if LeftDown:
                self.view[0] -= 10
                if self.view[0] < 0:
                    self.view[0] = 0
            if RightDown:
                self.view[0] += 10
            if self.view[0] > self.MapSize[0] - self.screen.get_size()[0]:
                self.view[0] = self.MapSize[0] - self.screen.get_size()[0]
            self.update()
            self.animate()

    def animate(self):
        size = self.screen.get_size()

        self.screen.fill(self.MapColor)

        for layer in self.layers:
            for s in layer:
                s.draw(self.screen, self.view)

        self.menu.draw_menu(self.screen)

        if self.buying is not None:
            self.draw_buy()
        elif self.selecting:
            surface = pygame.Surface([2 * self.selection_radius, 2 * self.selection_radius],
                                     flags=pygame.SRCALPHA)
            pygame.draw.circle(surface,
                               (255, 255, 255, 80),
                               [self.selection_radius, self.selection_radius],
                               float(self.selection_radius))
            self.screen.blit(surface,
                             [self.MousePosition[0] - self.selection_radius,
                              self.MousePosition[1] - self.selection_radius])
        elif self.targeting:
            surface = pygame.Surface([2 * self.selection_radius, 2 * self.selection_radius],
                                     flags=pygame.SRCALPHA)
            pygame.draw.circle(surface,
                               (255, 0, 0, 80),
                               [self.selection_radius, self.selection_radius],
                               float(self.selection_radius))
            self.screen.blit(surface,
                             [self.MousePosition[0] - self.selection_radius,
                              self.MousePosition[1] - self.selection_radius])

        # DRAW MINIMAP
        minimap = pygame.Surface([200, 200])
        minimap.fill(self.MapColor)
        for layer in self.layers:
            for s in layer:
                s.draw_map(minimap, self.MapSize)
        minimap_scale = 200 / self.MapSize[0], 200 / self.MapSize[1]
        pygame.draw.rect(minimap, [127, 127, 127],
                         [self.view[0] * minimap_scale[0], self.view[1] * minimap_scale[1],
                          size[0] * minimap_scale[0], size[1] * minimap_scale[1]],
                         width=2)
        self.screen.blit(minimap, [size[0] - 210, 10])
        pygame.draw.rect(self.screen, [100, 100, 100], [size[0] - 210 - 5, 10 - 5, 209, 209], width=5)

        self.screen.blit(pygame.image.load("assets/graphics/menu/homebutton.png"), [size[0] - 40, 215])

        # DRAW WIN/LOSE STATUS
        if self.status != 2:
            if self.status == 1:
                splash = pygame.image.load("assets/graphics/menu/winscreen.png")
                self.screen.blit(pygame.transform.scale(splash, size), (0,0))
                # You Win!
            elif self.status == 0:
                splash = pygame.image.load("assets/graphics/menu/losescreen.png")
                self.screen.blit(pygame.transform.scale(splash, size), (0, 0))
                # You Lose :(

        pygame.display.flip()

    def draw_buy(self):
        texture = self.Textures[self.buying]
        dest = [self.MousePosition[0] - texture.get_size()[0]//2,
                self.MousePosition[1] - texture.get_size()[1]//2]
        self.screen.blit(texture, dest)

    def exit(self):
        self.playing = False
        self.socket.send(b"exitcode\0\0\0\0\0\0\0\0", 0)
        pygame.quit()
        time.sleep(1)
        self.socket.close()

    def connect_to_server(self):
        if self.address is None:
            raise Exception("No address provided")
        self.socket.connect(self.address)
        self.socket.send(self.player_name.encode("utf8"), 0)
        mes = self.socket.recv(1024 * 1024, 0)
        self.MapSize = [int.from_bytes(mes[0:4], "little"),
                        int.from_bytes(mes[4:8], "little")
                        ]
        self.MapColor = (int.from_bytes(mes[8:12], "little"),
                         int.from_bytes(mes[12:16], "little"),
                         int.from_bytes(mes[16:20], "little")
                         )
        self.home = [int.from_bytes(mes[20:24], "little"),
                     int.from_bytes(mes[24:28], "little")
                     ]
        self.view = self.home[:]
        self.state_from_message(mes[28:])
        self.status = 2

    def update(self):
        self.socket.send(b"fullstateupdate;", 0)
        mes = self.socket.recv(1024 * 1024, 0)
        self.state_from_message(mes)

    def state_from_message(self, message: bytes):
        message = message[4:]
        self.status = int.from_bytes(message[0:4], "little")

        message = message[4:]
        self.menu.minerals = int.from_bytes(message[0:4], "little")

        message = message[4:]
        self.layers: list[list[Sprite]] = [[],[],[],[]]
        for s in range(len(message) // 12):
            p = message[s * 12 : s * 12 + 12]
            id = int.from_bytes(p[0:4], "little")
            x = int.from_bytes(p[4:8], "little")
            y = int.from_bytes(p[8:12], "little")

            ele = Sprite(id, x, y)
            self.layers[ele.get_layer()].append(ele)

    def message(self, code: bytes, val=0, x=0, y=0):
        message = code + val.to_bytes(4, "little") + x.to_bytes(4, "little") + y.to_bytes(4, "little")
        self.socket.send(message, 0)

    def click_minimap(self, location):
        size = self.screen.get_size()
        point = [(location[0] - (size[0] - 210)), (location[1] - 10)]
        real_point = [self.MapSize[0] * point[0] / 200, self.MapSize[1] * point[1] / 200]
        self.view = [int(real_point[0] - size[0] / 2), int(real_point[1] - size[1] / 2)]
        if self.view[1] < 0:
            self.view[1] = 0
        if self.view[1] > self.MapSize[1] - self.screen.get_size()[1]:
            self.view[1] = self.MapSize[1] - self.screen.get_size()[1]
        if self.view[0] < 0:
            self.view[0] = 0
        if self.view[0] > self.MapSize[0] - self.screen.get_size()[0]:
            self.view[0] = self.MapSize[0] - self.screen.get_size()[0]

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        player_name = sys.argv[1]
        ipAddress = sys.argv[2]
        port = int(sys.argv[3])
    else:
        player_name = input("Enter Name: ")
        ipAddress, port = input("Address: ").split(":")
        port = int(port)
    client = StuftCraftClient(player_name)
    address = (ipAddress, port)
    client.connect(address)
    client.play()
