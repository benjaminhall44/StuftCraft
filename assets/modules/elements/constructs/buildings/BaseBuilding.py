from assets.modules.elements.constructs.buildings.Building import *


class BaseBuilding(Building):
    def init(self):
        self.texture = TextureIdLib.BASE
        self.radius = 22.5
        self.health = 20
        self.cost = 10
        self.player.command_centers += 1

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
            self.alive = False
            self.player.command_centers -= 1
        else:
            self.Update(elements)