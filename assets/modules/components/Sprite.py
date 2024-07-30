import pygame

from assets.modules.libraries.SpriteLib import textures, layer_map, icons
class Sprite:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.pos = x,y

    def draw(self, screen, view):
        texture = self.get_texture()
        position = int(self.pos[0] - view[0] - texture.get_size()[0]//2), int(self.pos[1] - view[1] - texture.get_size()[1]//2)
        screen.blit(texture, position)

    def draw_map(self, screen: pygame.Surface, mapsize):
        size = screen.get_size()
        position = [int(size[0] * self.pos[0] / mapsize[0]), int(size[1] * self.pos[1] / mapsize[1])]
        color, points = self.get_icon()

        for x,y in points:
            screen.set_at([position[0] + x, position[1] + y], color)

    def get_texture(self):
        return textures[self.id]

    def get_icon(self):
        return icons[self.id]

    def get_layer(self):
        return layer_map[self.id]