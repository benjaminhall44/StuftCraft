from assets.modules.elements.constructs.troops.Troop import *


class BigManTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.BIGMAN
        self.radius = 18.0
        self.speed = 4.0
        self.health = 8
        self.cost = 8
        self.reload = 0
        self.target = None
        self.vision = 800
        self.range = 150
        self.charge = 0

    def attack(self, target, elements):
        self.charge += 1
        if self.charge >= 15:
            self.charge = 0
            elements.append(
                Projectile(TextureIdLib.LASER,
                           self.player,
                           self.position,
                           target.position,
                           7.0,
                           2.0,
                           2,
                           20
                           )
            )
