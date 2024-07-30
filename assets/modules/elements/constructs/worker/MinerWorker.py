from assets.modules.elements.constructs.worker.Worker import *
from assets.modules.elements.environment.MineralPile import MineralPile
from assets.modules.elements.constructs.buildings.BaseBuilding import BaseBuilding
class MinerWorker(Worker):
    MINING = 2
    def init(self):
        self.texture = TextureIdLib.MINER
        self.radius = 9.0
        self.speed = 10.0
        self.health = 5
        self.cost = 5
        self.progress = 0
        self.carrying = 0

        self.base = None
        self.mine = None

    def condition(self):
        if self.carrying == 0:
            return super().condition()
        else:
            if self.effect == NORMAL_EFFECT:
                return TextureIdLib.CARRYING
            else:
                return super().condition()

    def Update(self, elements):
        if self.mode == self.MINING:
            nearest = self.findNearest(MineralPile, elements)
            if nearest is not None and self.target is nearest and nearest.contents > 0:
                self.progress += 1
                if self.progress >= 20:
                    self.progress = 0
                    self.carrying = 1
                    nearest.contents -= 1
                    self.mode = self.WAITING
            else:
                self.progress = 0
                self.mode = self.WAITING
        elif self.mode == self.TRAVELING:
            if self.travel():
                if self.carrying == 0:
                    nearest = self.findNearest(MineralPile, elements)
                    if nearest is not None:
                        if self.target is nearest and isinstance(nearest, MineralPile) and nearest.contents > 0:
                            self.mode = self.MINING
                        else:
                            self.mine = nearest
                            self.target = nearest
                    else:
                        self.mine = None
                        self.mode = self.WAITING
                elif self.carrying == 1:
                    nearest = self.findNearest(BaseBuilding, elements, self.player)
                    if nearest is not None:
                        if self.target is nearest:
                            self.carrying = 0
                            self.player.minerals += 1
                            self.mode = self.WAITING
                        else:
                            self.base = nearest
                            self.target = nearest
                    else:
                        self.base = None
                        self.mode = self.WAITING
        elif self.mode == self.WAITING:
            if self.carrying == 0:
                if self.mine is not None:
                    self.target = self.mine
                    self.mode = self.TRAVELING
                else:
                    nearest = self.findNearest(MineralPile, elements)
                    if nearest is not None:
                        self.mine = nearest
                        self.target = nearest
                        self.mode = self.TRAVELING
            elif self.carrying == 1:
                if self.base is not None:
                    self.target = self.base
                    self.mode = self.TRAVELING
                else:
                    nearest = self.findNearest(BaseBuilding, elements)
                    if nearest is not None:
                        self.base = nearest
                        self.target = nearest
                        self.mode = self.TRAVELING

    def set_destination(self, location, radius, elements):
        for e in elements:
            if (e.position[0] - location[0]) ** 2 + (e.position[1] - location[1]) ** 2 < radius ** 2:
                if type(e) is MineralPile:
                    self.mine = e
                elif type(e) is BaseBuilding and e.player is self.player:
                    self.base = e

