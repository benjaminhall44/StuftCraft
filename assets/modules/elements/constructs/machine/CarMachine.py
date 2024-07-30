import random

from assets.modules.elements.constructs.machine.Machine import *
from assets.modules.elements.constructs.troops.Troop import Troop

class CarMachine(Machine):
    def init(self):
        self.texture = TextureIdLib.CAR
        self.radius = 20.0
        self.health = 12
        self.cost = 12
        self.speed = 16
        self.passengers = []
        self.WAITING = 0
        self.TRAVELING = 1
        self.mode = self.WAITING
        self.destination = []

    def Update(self, elements):
        if self.mode == self.WAITING:
            for e in elements:
                if len(self.passengers) < 6:
                    if isinstance(e, Troop) and e.player is self.player and e.mode == e.TRAVELING:
                        if (e.position[0] - self.position[0]) ** 2 + (e.position[1] - self.position[1]) ** 2 < (self.radius + e.radius) ** 2:
                            self.passengers.append(e)
                            elements.remove(e)
                else:
                    break
        elif self.mode == self.TRAVELING:
            if self.walk(self.destination) < self.speed:
                self.eject(elements)
                self.mode = self.WAITING

    def kill(self, elements):
        self.eject(elements)

    def eject(self, elements):
        for e in self.passengers:
            e.position = self.position[:]
            e.position[0] += random.randint(-int(self.radius), int(self.radius))
            e.position[1] += random.randint(-int(self.radius), int(self.radius))
            e.mode = e.ATTACKING
            elements.append(e)
        self.passengers = []
