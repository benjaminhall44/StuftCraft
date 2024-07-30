from assets.modules.elements.constructs.buildings.Building import *


class BaseBuilding(Building):
    def init(self):
        self.texture = TextureIdLib.BASE
        self.radius = 22.5
        self.health = 20
        self.cost = 10
        self.player.command_centers += 1

    def Update(self, elements):
        pass

    def kill(self, elements):
        self.player.command_centers -= 1
