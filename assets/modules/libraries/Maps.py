from assets.modules.components.Map import Map

from assets.modules.elements.constructs.worker.MinerWorker import MinerWorker
from assets.modules.elements.constructs.buildings.BaseBuilding import BaseBuilding

from assets.modules.elements.environment.MineralPile import MineralPile

PLAIN_ELEMENTS = (
        (MineralPile, ((500, 2500), 100)),
        (MineralPile, ((2500, 500), 100)),
        (MineralPile, ((2500, 2500), 100)),
        (MineralPile, ((500, 500), 100)),

        (MineralPile, ((1500, 1500), 500))
    )
DESERT_ELEMENTS = (
        (MineralPile, ((500, 2500), 100)),
        (MineralPile, ((2500, 500), 100)),
        (MineralPile, ((2500, 2500), 100)),
        (MineralPile, ((500, 500), 100)),
)
CAVE_ELEMENTS = (
        (MineralPile, ((500, 2500), 100)),
        (MineralPile, ((2500, 500), 100)),
        (MineralPile, ((2500, 2500), 100)),
        (MineralPile, ((500, 500), 100)),

        (MineralPile, ((1500, 2500), 200)),
        (MineralPile, ((1500, 500), 200)),
        (MineralPile, ((2500, 1500), 200)),
        (MineralPile, ((500, 1500), 200)),

        (MineralPile, ((1500, 1500), 500))
)

PlainMap2player = Map(
    (3000, 3000),
    (0, 255, 0),
    ((0, 2150), (2000, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (0, (400, 2500))),
        (MinerWorker, (1, (2400, 500))),
        *PLAIN_ELEMENTS
    )
)

PlainMap3player = Map(
    (3000, 3000),
    (0, 255, 0),
    ((0, 2150), (2000, 150), (0, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),
        *PLAIN_ELEMENTS
    )
)

PlainMap4player = Map(
    (3000, 3000),
    (0, 255, 0),
    ((0, 2150), (2000, 150), (0, 150), (2000, 2150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),

        (BaseBuilding, (3, (2300, 2500))),
        (MinerWorker, (3, (2400, 2500))),
        *PLAIN_ELEMENTS
    )
)

DesertMap2player = Map(
    (3000, 3000),
    (255, 255, 0),
    ((0, 2150), (2000, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (0, (400, 2500))),
        (MinerWorker, (1, (2400, 500))),
        *DESERT_ELEMENTS
    )
)

DesertMap3player = Map(
    (3000, 3000),
    (255, 255, 0),
    ((0, 2150), (2000, 150), (0, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),
        *DESERT_ELEMENTS
    )
)

DesertMap4player = Map(
    (3000, 3000),
    (255, 255, 0),
    ((0, 2150), (2000, 150), (0, 150), (2000, 2150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),

        (BaseBuilding, (3, (2300, 2500))),
        (MinerWorker, (3, (2400, 2500))),
        *DESERT_ELEMENTS
    )
)

CaveMap2player = Map(
    (3000, 3000),
    (128, 64, 0),
    ((0, 2150), (2000, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (0, (400, 2500))),
        (MinerWorker, (1, (2400, 500))),
        *CAVE_ELEMENTS
    )
)

CaveMap3player = Map(
    (3000, 3000),
    (128, 64, 0),
    ((0, 2150), (2000, 150), (0, 150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),
        *CAVE_ELEMENTS
    )
)

CaveMap4player = Map(
    (3000, 3000),
    (128, 64, 0),
    ((0, 2150), (2000, 150), (0, 150), (2000, 2150)),
    (
        (BaseBuilding, (0, (300, 2500))),
        (MinerWorker, (0, (400, 2500))),

        (BaseBuilding, (1, (2300, 500))),
        (MinerWorker, (1, (2400, 500))),

        (BaseBuilding, (2, (300, 500))),
        (MinerWorker, (2, (400, 500))),

        (BaseBuilding, (3, (2300, 2500))),
        (MinerWorker, (3, (2400, 2500))),
        *CAVE_ELEMENTS
    )
)

Maps ={
    "Plain":{
        2:PlainMap2player,
        3:PlainMap3player,
        4:PlainMap4player
    },
    "Desert":{
        2:DesertMap2player,
        3:DesertMap3player,
        4:DesertMap4player
    },
    "Cave":{
        2:CaveMap2player,
        3:CaveMap3player,
        4:CaveMap4player
    },
}