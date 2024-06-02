import pygame

from Vector import Vector

class Element:
    def __init__(self):
        self.texture = 0
        self.position = Vector(100,100)

    def update(self):
        self.position = self.position + Vector(10, 0)

    def is_visible(self):
        return True

    def get_id(self):
        return self.texture

    def draw_position(self):
        return self.position


