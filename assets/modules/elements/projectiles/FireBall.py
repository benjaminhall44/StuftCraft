from assets.modules.elements.projectiles.Projectile import *
from assets.modules.elements.constructs.Construct import BURN_EFFECT


class FireBall(Projectile):
    def collision(self, e: Construct, elements: list[Element]):
        e.health -= self.damage
        e.effect = BURN_EFFECT
        e.effect_remaining = 50
        self.alive = False
