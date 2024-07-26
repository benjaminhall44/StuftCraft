from assets.modules.elements.constructs.troops.Troop import *


class LaserEagleTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.LASEREAGLE
        self.radius = 15.0
        self.speed = 7.0
        self.health = 5
        self.cost = 7
        self.reload = 0
        self.target = None
        self.vision = 1000
        self.range = 200
        self.charge = 0

    def attack(self, target, elements):
        self.charge += 1
        if self.charge >= 10:
            self.charge = 0
            elements.append(
                Projectile(TextureIdLib.LASER,
                           self.player,
                           self.position,
                           target.position,
                           7.0,
                           2.0,
                           1,
                           40
                           )
            )
