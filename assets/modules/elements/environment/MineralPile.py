from assets.modules.elements.Element import *

class MineralPile (Element):
    def __init__(self, pos, contents):
        super().__init__(pos)
        self.texture = TextureIdLib.MINERALPILE
        self.contents: int = contents
        self.radius = 60.0

    def update(self, elements):
        if self.contents <= 0:
            self.alive = False
