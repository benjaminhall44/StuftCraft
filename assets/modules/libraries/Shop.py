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

ShopContents = [
    {"Cost": 10, "Class": BaseBuilding},
    {"Cost": 3, "Class":ThreeTroop},
    {"Cost": 4, "Class":FourTroop},
    {"Cost": 6, "Class":ManTroop},
    {"Cost": 7, "Class":LaserEagleTroop},
    {"Cost": 8, "Class": BigManTroop},
    {"Cost": 9, "Class": SpiderTroop},
    {"Cost": 11, "Class": FlyingTankTroop},
    {"Cost": 5, "Class": MinerWorker},
    {"Cost": 12, "Class": CarMachine},
    {"Cost": 16, "Class": DragonTroop}
]