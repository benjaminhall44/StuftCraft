from assets.modules.elements.constructs.worker.Worker import *
from assets.modules.elements.environment.MineralPile import MineralPile
from assets.modules.elements.constructs.buildings.BaseBuilding import BaseBuilding
class MinerWorker(Worker):
    def init(self):
        self.texture = TextureIdLib.MINER
        self.radius = 9.0
        self.speed = 10.0
        self.health = 5
        self.cost = 5
        self.progress = 0
        self.traveling = False
        self.carrying = 0

    def condition(self):
        if self.carrying == 0:
            return super().condition()
        else:
            if self.effect == NORMAL_EFFECT:
                return TextureIdLib.CARRYING
            else:
                return super().condition()

    def Update(self, elements):
        if not self.traveling:
            if self.carrying == 0:
                nearest = self.findNearest(MineralPile, elements)
                if nearest is not None:
                    self.target = nearest
                    self.traveling = True
            elif self.carrying == 1:
                nearest = self.findNearest(BaseBuilding, elements, self.player)
                if nearest is not None:
                    self.target = nearest
                    self.traveling = True
        else:
            if self.travel():
                if self.carrying == 0:
                    nearest = self.findNearest(MineralPile, elements)
                    if nearest is not None:
                        if self.target == nearest:
                            if isinstance(nearest, MineralPile):
                                if nearest.contents > 0:
                                    self.progress += 1
                                    if self.progress >= 20:
                                        self.progress = 0
                                        self.carrying = 1
                                        nearest.contents -= 1
                                        self.traveling = False
                        else:
                            self.target = nearest
                    self.traveling = False
                elif self.carrying == 1:
                    nearest = self.findNearest(BaseBuilding, elements, self.player)
                    if nearest is not None:
                        if self.target == nearest:
                            self.carrying = 0
                            self.player.minerals += 1
                            self.traveling = False
                        else:
                            self.target = nearest
                    else:
                        self.traveling = False
