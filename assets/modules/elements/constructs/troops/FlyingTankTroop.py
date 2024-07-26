from assets.modules.elements.constructs.troops.Troop import *
from assets.modules.elements.projectiles.Missile import Missile

class FlyingTankTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.FLYINGTANK
        self.radius = 15.0
        self.speed = 7.0
        self.health = 11
        self.cost = 11
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
                Missile(TextureIdLib.MISSILE,
                        self.player,
                        self.position,
                        target.position,
                        6.0,
                        4.0,
                        1,
                        20,
                        30
                        )
            )
