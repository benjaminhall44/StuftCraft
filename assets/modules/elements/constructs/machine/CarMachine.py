from assets.modules.elements.constructs.troops.Troop import *


class CarMachine(Troop):
    def init(self):
        self.texture = TextureIdLib.CAR
        self.radius = 20.0
        self.health = 12
        self.cost = 12

    def Update(self, elements):
        pass