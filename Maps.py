from Map import Map

from assets.modules.elements.constructs.troops.ThreeTroop import ThreeTroop
from assets.modules.elements.constructs.troops.FourTroop import FourTroop
from assets.modules.elements.constructs.worker.MinerWorker import MinerWorker
from assets.modules.elements.constructs.troops.ManTroop import ManTroop
from assets.modules.elements.constructs.troops.LaserEagleTroop import LaserEagleTroop
from assets.modules.elements.constructs.troops.BigManTroop import BigManTroop
from assets.modules.elements.constructs.troops.SpiderTroop import SpiderTroop
from assets.modules.elements.constructs.buildings.BaseBuilding import BaseBuilding
from assets.modules.elements.constructs.troops.FlyingTankTroop import FlyingTankTroop
from assets.modules.elements.constructs.machine.CarMachine import CarMachine
from assets.modules.elements.constructs.troops.DragonTroop import DragonTroop

from assets.modules.elements.environment.MineralPile import MineralPile

PlainMap = Map(
    (3000, 3000),
    ((100, 1900), (1900, 100)),
    (
        (MineralPile, ((400, 2400), 100)),
        (MineralPile, ((2200, 600), 100)),
        (BaseBuilding, (0, (200, 2400))),
        (BaseBuilding, (1, (2000, 600))),
        (MinerWorker, (0, (300, 2400))),
        (MinerWorker, (1, (2100, 600)))
    )
)