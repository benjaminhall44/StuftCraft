from assets.modules.elements.Element import *
from assets.modules.components.Player import Player
import random

NORMAL_EFFECT = TextureIdLib.NORMAL
WEBBED_EFFECT = TextureIdLib.WEBBED
BURN_EFFECT = TextureIdLib.BURNING

class Construct(Element):
    health: int
    speed: int
    cost: int
    effect: int
    effect_counter: int
    effect_remaining: int

    WAITING = 0
    TRAVELING = 1

    def __init__(self, player, pos):
        super().__init__(pos)
        self.player: Player = player
        self.effect = 0
        self.effect_counter = 0
        self.effect_remaining = 0
        self.mode = 0
        self.init()

    def init(self):
        raise NotImplemented

    def update(self, elements):
        if self.effect != NORMAL_EFFECT:
            self.effect_counter += 1
            if self.effect == BURN_EFFECT and self.effect_counter >= 10:
                self.health -= 1
                self.effect_counter = 0
            self.effect_remaining -= 1
            if self.effect_remaining <= 0:
                self.effect = 0
                self.effect_counter = 0
                self.effect_remaining = 0

        if self.health <= 0:
            self.kill(elements)
            self.alive = False
        else:
            self.Update(elements)

    def Update(self, elements: list[Element]):
        raise NotImplemented

    def kill(self, elements):
        pass

    def condition(self):
        return self.effect

    def get_texture(self):
        return self.texture | self.condition() | self.player.id

    @staticmethod
    def place_condition(player: Player, position: list[int], elements: list[Element]):
        from assets.modules.elements.constructs.buildings.BaseBuilding import BaseBuilding
        for e in elements:
            if isinstance(e, BaseBuilding):
                if e.player is player:
                    if (position[0] - e.position[0]) ** 2 + (position[1] - e.position[1]) ** 2 < 40000:
                        return True
        return False

    def walk(self, location):
        togo = (location[0] - self.position[0],
                location[1] - self.position[1])
        distance = (togo[0] ** 2 + togo[1] ** 2) ** .5
        speed = self.speed
        if self.effect == WEBBED_EFFECT:
            speed *= 0.5
        if distance > speed:
            self.position[0] += togo[0] * speed / distance
            self.position[1] += togo[1] * speed / distance
        return distance

    def set_destination(self, location, radius, elements):
        self.mode = self.TRAVELING
        xerror = random.randint(-radius, radius)
        yradius = int((radius ** 2 - xerror ** 2) ** .5)
        yerror = random.randint(-yradius, yradius)
        self.destination = [location[0] + xerror, location[1] + yerror]