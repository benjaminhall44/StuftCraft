from assets.modules.elements.projectiles.Projectile import *
from assets.modules.elements.environment.VisualElement import VisualElement

class Missile(Projectile):
    def __init__(self, texture, team: Player, pos, destination, speed, radius, damage, life, blast_radius):
        super().__init__(texture, team, pos, destination, speed, radius, damage, life)
        self.blast_radius = blast_radius

    def collision(self, e: Construct, elements: list[Element]):
        for e in elements:
            if isinstance(e, Construct) and e.player is not self.team:
                if self.distanceTo(e) < self.blast_radius + e.radius:
                    e.health -= self.damage
        self.alive = False
        elements.append(VisualElement(self.position, TextureIdLib.EXPLOSION, 4))
