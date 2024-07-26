import TextureIdLib
from assets.modules.elements.constructs.troops.Troop import *

class ThreeTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.THREE
        self.radius = 10.0
        self.speed = 3.0
        self.health = 3
        self.cost = 3
        self.reload = 0
        self.target = None
        self.vision = 500
        self.range = 100
        self.charge = 0

    def attack(self, target, elements):
        self.charge += 1
        if self.charge >= 20:
            self.charge = 0
            elements.append(
                Projectile(TextureIdLib.LASER,
                           self.player,
                           self.position,
                           target.position,
                           7.0,
                           2.0,
                           1,
                           20
                           )
            )
