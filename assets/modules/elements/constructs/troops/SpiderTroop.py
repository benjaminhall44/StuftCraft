from assets.modules.elements.constructs.troops.Troop import *
from assets.modules.elements.projectiles.Web import *

class SpiderTroop(Troop):
    def init(self):
        self.texture = TextureIdLib.SPIDER
        self.radius = 15.0
        self.speed = 5.0
        self.health = 4
        self.cost = 9
        self.reload = 0
        self.target = None
        self.vision = 600
        self.range = 150
        self.charge = 0

    def attack(self, target, elements):
        # TODO web attack
        self.charge += 1
        if self.charge >= 10:
            self.charge = 0
            elements.append(
                Web(TextureIdLib.WEB,
                    self.player,
                    self.position,
                    target.position,
                    10.0,
                    4.0,
                    1,
                    20
                    )
            )
