from assets.modules.elements.constructs.troops.Troop import *
from assets.modules.elements.projectiles.FireBall import FireBall

class DragonTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.DRAGON
        self.radius = 15.0
        self.speed = 5.0
        self.health = 16
        self.cost = 16
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
                FireBall(TextureIdLib.FIREBALL,
                         self.player,
                         self.position,
                         target.position,
                         7.0,
                         4.0,
                         3,
                         20)
            )