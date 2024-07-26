from assets.modules.elements.constructs.Construct import *
from assets.modules.elements.projectiles.Projectile import *

class Troop(Construct):
    speed: float
    vision: float
    range: float

    target: Element|None
    destination: list[int]
    mode = 0

    ATTACKING = 0
    TRAVELING = 1

    def attack(self, target: Element, elements: list[Element]):
        raise NotImplemented

    def Update(self, elements):
        if self.mode == self.ATTACKING:
            if self.target is not None and self.target.alive:
                dist = self.distanceTo(self.target)
                if dist < self.range:
                    self.attack(self.target, elements)
                elif dist < self.vision:
                    self.pursue(self.target)
                else:
                    self.target = None
            else:
                target = self.findEnemy(elements)
                if target is not None and self.distanceTo(target) < self.vision:
                    self.target = target

        elif self.mode == self.TRAVELING:
            if self.walk(self.destination) < self.speed:
                self.mode = self.ATTACKING

    def distanceTo(self, target: Element):
        togo = (target.position[0] - self.position[0],
                target.position[1] - self.position[1])
        return (togo[0] ** 2 + togo[1] ** 2) ** .5

    def pursue(self, target):
        self.walk(target.position)

    def findEnemy(self, elements: list[Element]):
        nearest = None
        distance = 1000000000000
        for e in elements:
            if (isinstance(e, Construct) and e.player is not self.player):
                dist = (e.position[0] - self.position[0]) ** 2 + (e.position[1] - self.position[1]) ** 2
                if dist < distance:
                    nearest = e
                    distance = dist
        return nearest

