import pygame

from Vector import Vector
import TextureIdLib

class Element:
    def __init__(self, pos):
        self.texture = 0
        self.position = list(pos)
        self.radius = 0
        self.alive = True

    def update(self, elements):
        raise NotImplemented

    def is_visible(self):
        return True

    def get_texture(self):
        return self.texture

    def draw_position(self):
        return [int(self.position[0]), int(self.position[1])]


