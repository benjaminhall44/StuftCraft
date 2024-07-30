from assets.modules.elements.Element import *

class VisualElement(Element):
    def __init__(self, pos, texture, duration):
        super().__init__(pos)
        self.texture = texture
        self.duration = duration

    def update(self, elements):
        self.duration -= 1
        if self.duration <= 0:
            self.alive = False
