from assets.modules.elements.projectiles.Projectile import *
from assets.modules.elements.constructs.Construct import WEBBED_EFFECT

class Web(Projectile):
    def collision(self, e: Construct, elements: list[Element]):
        e.health -= self.damage
        e.effect = WEBBED_EFFECT
        e.effect_remaining = 100
        self.alive = False
