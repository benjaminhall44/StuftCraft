from assets.modules.elements.Element import *

class MineralPile (Element):
    def __init__(self, pos, contents):
        super().__init__(pos)
        self.texture = TextureIdLib.SMALLMINERALPILE
        self.contents: int = contents
        self.radius = 60.0

    def update(self, elements):
        if self.contents <= 0:
            self.alive = False
        elif self.contents <= 100:
            self.radius = 60
        elif self.contents <= 200:
            self.radius = 120
        else:
            self.radius = 180

    def get_texture(self):
        if self.contents > 200:
            return TextureIdLib.LARGEMINERALPILE
        elif self.contents > 100:
            return TextureIdLib.MEDIUMMINERALPILE
        else:
            return TextureIdLib.SMALLMINERALPILE
