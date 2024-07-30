from assets.modules.elements.Element import *
from assets.modules.elements.constructs.Construct import Construct
from assets.modules.components.Player import Player

class Projectile(Element):
    def __init__(self, texture, team: Player, pos, destination, speed, radius, damage, life):
        super().__init__(pos)
        self.team = team
        self.texture = texture | team.id

        togo = (destination[0] - self.position[0],
                destination[1] - self.position[1])
        distance = (togo[0] ** 2 + togo[1] ** 2) ** .5
        self.velocity = [togo[0] * speed / distance, togo[1] * speed / distance]
        self.radius = radius
        self.damage = damage
        self.age = 0
        self.life = life
    def update(self, elements: list[Element]):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        for e in elements:
            if isinstance(e, Construct) and e.player is not self.team:
                if self.distanceTo(e) < self.radius + e.radius:
                    self.collision(e, elements)
                    break
        self.age += 1
        if self.age >= self.life:
            self.alive = False

    def distanceTo(self, target: Element):
        togo = (target.position[0] - self.position[0],
                target.position[1] - self.position[1])
        return (togo[0] ** 2 + togo[1] ** 2) ** .5

    def collision(self, e: Construct, elements: list[Element]):
        e.health -= self.damage
        self.alive = False


