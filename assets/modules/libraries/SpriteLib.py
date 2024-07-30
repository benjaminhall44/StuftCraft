import pygame
from assets.modules.libraries.TextureIdLib import *


textures: list[pygame.surface.Surface|None] = [None] * 1024

textures[THREE | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/three/red/normal.png")
textures[THREE | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/three/red/webbed.png")
textures[THREE | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/three/red/burning.png")
textures[THREE | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/three/blue/normal.png")
textures[THREE | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/three/blue/webbed.png")
textures[THREE | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/three/blue/burning.png")
textures[THREE | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/troops/three/yellow/normal.png")
textures[THREE | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/three/yellow/webbed.png")
textures[THREE | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/three/yellow/burning.png")
textures[THREE | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/three/green/normal.png")
textures[THREE | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/three/green/webbed.png")
textures[THREE | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/three/green/burning.png")

textures[FOUR | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/four/red/normal.png")
textures[FOUR | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/four/red/webbed.png")
textures[FOUR | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/four/red/burning.png")
textures[FOUR | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/four/blue/normal.png")
textures[FOUR | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/four/blue/webbed.png")
textures[FOUR | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/four/blue/burning.png")
textures[FOUR | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/troops/four/yellow/normal.png")
textures[FOUR | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/four/yellow/webbed.png")
textures[FOUR | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/four/yellow/burning.png")
textures[FOUR | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/four/green/normal.png")
textures[FOUR | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/four/green/webbed.png")
textures[FOUR | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/four/green/burning.png")

textures[MINER | RED | NORMAL] = pygame.image.load("assets/graphics/elements/workers/miner/red/normal.png")
textures[MINER | RED | WEBBED] = pygame.image.load("assets/graphics/elements/workers/miner/red/webbed.png")
textures[MINER | RED | BURNING] = pygame.image.load("assets/graphics/elements/workers/miner/red/burning.png")
textures[MINER | RED | CARRYING] = pygame.image.load("assets/graphics/elements/workers/miner/red/carrying.png")
textures[MINER | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/workers/miner/blue/normal.png")
textures[MINER | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/workers/miner/blue/webbed.png")
textures[MINER | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/workers/miner/blue/burning.png")
textures[MINER | BLUE | CARRYING] = pygame.image.load("assets/graphics/elements/workers/miner/blue/carrying.png")
textures[MINER | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/workers/miner/yellow/normal.png")
textures[MINER | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/workers/miner/yellow/webbed.png")
textures[MINER | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/workers/miner/yellow/burning.png")
textures[MINER | YELLOW | CARRYING] = pygame.image.load("assets/graphics/elements/workers/miner/yellow/carrying.png")
textures[MINER | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/workers/miner/green/normal.png")
textures[MINER | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/workers/miner/green/webbed.png")
textures[MINER | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/workers/miner/green/burning.png")
textures[MINER | GREEN | CARRYING] = pygame.image.load("assets/graphics/elements/workers/miner/green/carrying.png")


textures[MAN | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/man/red/normal.png")
textures[MAN | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/man/red/webbed.png")
textures[MAN | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/man/red/burning.png")
textures[MAN | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/man/blue/normal.png")
textures[MAN | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/man/blue/webbed.png")
textures[MAN | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/man/blue/burning.png")
textures[MAN | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/troops/man/yellow/normal.png")
textures[MAN | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/man/yellow/webbed.png")
textures[MAN | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/man/yellow/burning.png")
textures[MAN | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/man/green/normal.png")
textures[MAN | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/man/green/webbed.png")
textures[MAN | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/man/green/burning.png")

textures[LASEREAGLE | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/lasereagle/red/normal.png")
textures[LASEREAGLE | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/lasereagle/red/webbed.png")
textures[LASEREAGLE | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/lasereagle/red/burning.png")
textures[LASEREAGLE | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/lasereagle/blue/normal.png")
textures[LASEREAGLE | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/lasereagle/blue/webbed.png")
textures[LASEREAGLE | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/lasereagle/blue/burning.png")
textures[LASEREAGLE | YELLOW | NORMAL] = pygame.image.load(
    "assets/graphics/elements/troops/lasereagle/yellow/normal.png")
textures[LASEREAGLE | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/lasereagle/yellow/webbed.png")
textures[LASEREAGLE | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/lasereagle/yellow/burning.png")
textures[LASEREAGLE | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/lasereagle/green/normal.png")
textures[LASEREAGLE | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/lasereagle/green/webbed.png")
textures[LASEREAGLE | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/lasereagle/green/burning.png")

textures[BIGMAN | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/bigman/red/normal.png")
textures[BIGMAN | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/bigman/red/webbed.png")
textures[BIGMAN | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/bigman/red/burning.png")
textures[BIGMAN | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/bigman/blue/normal.png")
textures[BIGMAN | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/bigman/blue/webbed.png")
textures[BIGMAN | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/bigman/blue/burning.png")
textures[BIGMAN | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/troops/bigman/yellow/normal.png")
textures[BIGMAN | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/bigman/yellow/webbed.png")
textures[BIGMAN | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/bigman/yellow/burning.png")
textures[BIGMAN | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/bigman/green/normal.png")
textures[BIGMAN | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/bigman/green/webbed.png")
textures[BIGMAN | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/bigman/green/burning.png")

textures[SPIDER | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/spider/red/normal.png")
textures[SPIDER | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/spider/red/webbed.png")
textures[SPIDER | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/spider/red/burning.png")
textures[SPIDER | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/spider/blue/normal.png")
textures[SPIDER | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/spider/blue/webbed.png")
textures[SPIDER | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/spider/blue/burning.png")
textures[SPIDER | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/troops/spider/yellow/normal.png")
textures[SPIDER | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/spider/yellow/webbed.png")
textures[SPIDER | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/spider/yellow/burning.png")
textures[SPIDER | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/spider/green/normal.png")
textures[SPIDER | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/spider/green/webbed.png")
textures[SPIDER | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/spider/green/burning.png")

textures[BASE | RED | NORMAL] = pygame.image.load("assets/graphics/elements/buildings/base/red/normal.png")
textures[BASE | RED | WEBBED] = pygame.image.load("assets/graphics/elements/buildings/base/red/webbed.png")
textures[BASE | RED | BURNING] = pygame.image.load("assets/graphics/elements/buildings/base/red/burning.png")
textures[BASE | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/buildings/base/blue/normal.png")
textures[BASE | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/buildings/base/blue/webbed.png")
textures[BASE | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/buildings/base/blue/burning.png")
textures[BASE | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/buildings/base/yellow/normal.png")
textures[BASE | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/buildings/base/yellow/webbed.png")
textures[BASE | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/buildings/base/yellow/burning.png")
textures[BASE | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/buildings/base/green/normal.png")
textures[BASE | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/buildings/base/green/webbed.png")
textures[BASE | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/buildings/base/green/burning.png")

textures[FLYINGTANK | RED | NORMAL] = pygame.image.load("assets/graphics/elements/troops/flyingtank/red/normal.png")
textures[FLYINGTANK | RED | WEBBED] = pygame.image.load("assets/graphics/elements/troops/flyingtank/red/webbed.png")
textures[FLYINGTANK | RED | BURNING] = pygame.image.load("assets/graphics/elements/troops/flyingtank/red/burning.png")
textures[FLYINGTANK | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/troops/flyingtank/blue/normal.png")
textures[FLYINGTANK | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/troops/flyingtank/blue/webbed.png")
textures[FLYINGTANK | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/troops/flyingtank/blue/burning.png")
textures[FLYINGTANK | YELLOW | NORMAL] = pygame.image.load(
    "assets/graphics/elements/troops/flyingtank/yellow/normal.png")
textures[FLYINGTANK | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/troops/flyingtank/yellow/webbed.png")
textures[FLYINGTANK | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/troops/flyingtank/yellow/burning.png")
textures[FLYINGTANK | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/troops/flyingtank/green/normal.png")
textures[FLYINGTANK | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/troops/flyingtank/green/webbed.png")
textures[FLYINGTANK | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/troops/flyingtank/green/burning.png")

textures[CAR | RED | NORMAL] = pygame.image.load("assets/graphics/elements/machines/car/red/normal.png")
textures[CAR | RED | WEBBED] = pygame.image.load("assets/graphics/elements/machines/car/red/webbed.png")
textures[CAR | RED | BURNING] = pygame.image.load("assets/graphics/elements/machines/car/red/burning.png")
textures[CAR | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/machines/car/blue/normal.png")
textures[CAR | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/machines/car/blue/webbed.png")
textures[CAR | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/machines/car/blue/burning.png")
textures[CAR | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/machines/car/yellow/normal.png")
textures[CAR | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/machines/car/yellow/webbed.png")
textures[CAR | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/machines/car/yellow/burning.png")
textures[CAR | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/machines/car/green/normal.png")
textures[CAR | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/machines/car/green/webbed.png")
textures[CAR | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/machines/car/green/burning.png")

textures[DRAGON | RED | NORMAL] = pygame.image.load("assets/graphics/elements/research/dragon/red/normal.png")
textures[DRAGON | RED | WEBBED] = pygame.image.load("assets/graphics/elements/research/dragon/red/webbed.png")
textures[DRAGON | RED | BURNING] = pygame.image.load("assets/graphics/elements/research/dragon/red/burning.png")
textures[DRAGON | BLUE | NORMAL] = pygame.image.load("assets/graphics/elements/research/dragon/blue/normal.png")
textures[DRAGON | BLUE | WEBBED] = pygame.image.load("assets/graphics/elements/research/dragon/blue/webbed.png")
textures[DRAGON | BLUE | BURNING] = pygame.image.load("assets/graphics/elements/research/dragon/blue/burning.png")
textures[DRAGON | YELLOW | NORMAL] = pygame.image.load("assets/graphics/elements/research/dragon/yellow/normal.png")
textures[DRAGON | YELLOW | WEBBED] = pygame.image.load("assets/graphics/elements/research/dragon/yellow/webbed.png")
textures[DRAGON | YELLOW | BURNING] = pygame.image.load("assets/graphics/elements/research/dragon/yellow/burning.png")
textures[DRAGON | GREEN | NORMAL] = pygame.image.load("assets/graphics/elements/research/dragon/green/normal.png")
textures[DRAGON | GREEN | WEBBED] = pygame.image.load("assets/graphics/elements/research/dragon/green/webbed.png")
textures[DRAGON | GREEN | BURNING] = pygame.image.load("assets/graphics/elements/research/dragon/green/burning.png")

textures[LASER | RED] = pygame.image.load("assets/graphics/elements/projectiles/laser/red.png")
textures[LASER | BLUE] = pygame.image.load("assets/graphics/elements/projectiles/laser/blue.png")
textures[LASER | YELLOW] = pygame.image.load("assets/graphics/elements/projectiles/laser/yellow.png")
textures[LASER | GREEN] = pygame.image.load("assets/graphics/elements/projectiles/laser/green.png")

textures[WEB | RED] = pygame.image.load("assets/graphics/elements/projectiles/web.png")
textures[WEB | BLUE] = textures[WEB | RED]
textures[WEB | YELLOW] = textures[WEB | RED]
textures[WEB | GREEN] = textures[WEB | RED]

textures[FIREBALL | RED] = pygame.image.load("assets/graphics/elements/projectiles/fireball.png")
textures[FIREBALL | BLUE] = textures[FIREBALL | RED]
textures[FIREBALL | YELLOW] = textures[FIREBALL | RED]
textures[FIREBALL | GREEN] = textures[FIREBALL | RED]

textures[MISSILE | RED] = pygame.image.load("assets/graphics/elements/projectiles/missile/red.png")
textures[MISSILE | BLUE] = pygame.image.load("assets/graphics/elements/projectiles/missile/blue.png")
textures[MISSILE | YELLOW] = pygame.image.load("assets/graphics/elements/projectiles/missile/yellow.png")
textures[MISSILE | GREEN] = pygame.image.load("assets/graphics/elements/projectiles/missile/green.png")

textures[EXPLOSION] = pygame.image.load("assets/graphics/elements/projectiles/explosion.png")

textures[SMALLMINERALPILE] = pygame.image.load("assets/graphics/elements/environment/mineralpile.png")
textures[MEDIUMMINERALPILE] = pygame.image.load("assets/graphics/elements/environment/mediummineralpile.png")
textures[LARGEMINERALPILE] = pygame.image.load("assets/graphics/elements/environment/largemineralpile.png")

GROUND_LAYER = 0
BASE_LAYER = 1
TROOP_LAYER = 2
SKY_LAYER = 3

layer_map: list[int] = [0] * 1024

layer_map[THREE | RED | NORMAL] = TROOP_LAYER
layer_map[THREE | RED | WEBBED] = TROOP_LAYER
layer_map[THREE | RED | BURNING] = TROOP_LAYER
layer_map[THREE | BLUE | NORMAL] = TROOP_LAYER
layer_map[THREE | BLUE | WEBBED] = TROOP_LAYER
layer_map[THREE | BLUE | BURNING] = TROOP_LAYER
layer_map[THREE | YELLOW | NORMAL] = TROOP_LAYER
layer_map[THREE | YELLOW | WEBBED] = TROOP_LAYER
layer_map[THREE | YELLOW | BURNING] = TROOP_LAYER
layer_map[THREE | GREEN | NORMAL] = TROOP_LAYER
layer_map[THREE | GREEN | WEBBED] = TROOP_LAYER
layer_map[THREE | GREEN | BURNING] = TROOP_LAYER

layer_map[FOUR | RED | NORMAL] = TROOP_LAYER
layer_map[FOUR | RED | WEBBED] = TROOP_LAYER
layer_map[FOUR | RED | BURNING] = TROOP_LAYER
layer_map[FOUR | BLUE | NORMAL] = TROOP_LAYER
layer_map[FOUR | BLUE | WEBBED] = TROOP_LAYER
layer_map[FOUR | BLUE | BURNING] = TROOP_LAYER
layer_map[FOUR | YELLOW | NORMAL] = TROOP_LAYER
layer_map[FOUR | YELLOW | WEBBED] = TROOP_LAYER
layer_map[FOUR | YELLOW | BURNING] = TROOP_LAYER
layer_map[FOUR | GREEN | NORMAL] = TROOP_LAYER
layer_map[FOUR | GREEN | WEBBED] = TROOP_LAYER
layer_map[FOUR | GREEN | BURNING] = TROOP_LAYER

layer_map[MINER | RED | NORMAL] = TROOP_LAYER
layer_map[MINER | RED | WEBBED] = TROOP_LAYER
layer_map[MINER | RED | BURNING] = TROOP_LAYER
layer_map[MINER | RED | CARRYING] = TROOP_LAYER
layer_map[MINER | BLUE | NORMAL] = TROOP_LAYER
layer_map[MINER | BLUE | WEBBED] = TROOP_LAYER
layer_map[MINER | BLUE | BURNING] = TROOP_LAYER
layer_map[MINER | BLUE | CARRYING] = TROOP_LAYER
layer_map[MINER | YELLOW | NORMAL] = TROOP_LAYER
layer_map[MINER | YELLOW | WEBBED] = TROOP_LAYER
layer_map[MINER | YELLOW | BURNING] = TROOP_LAYER
layer_map[MINER | YELLOW | CARRYING] = TROOP_LAYER
layer_map[MINER | GREEN | NORMAL] = TROOP_LAYER
layer_map[MINER | GREEN | WEBBED] = TROOP_LAYER
layer_map[MINER | GREEN | BURNING] = TROOP_LAYER
layer_map[MINER | GREEN | CARRYING] = TROOP_LAYER


layer_map[MAN | RED | NORMAL] = TROOP_LAYER
layer_map[MAN | RED | WEBBED] = TROOP_LAYER
layer_map[MAN | RED | BURNING] = TROOP_LAYER
layer_map[MAN | BLUE | NORMAL] = TROOP_LAYER
layer_map[MAN | BLUE | WEBBED] = TROOP_LAYER
layer_map[MAN | BLUE | BURNING] = TROOP_LAYER
layer_map[MAN | YELLOW | NORMAL] = TROOP_LAYER
layer_map[MAN | YELLOW | WEBBED] = TROOP_LAYER
layer_map[MAN | YELLOW | BURNING] = TROOP_LAYER
layer_map[MAN | GREEN | NORMAL] = TROOP_LAYER
layer_map[MAN | GREEN | WEBBED] = TROOP_LAYER
layer_map[MAN | GREEN | BURNING] = TROOP_LAYER

layer_map[LASEREAGLE | RED | NORMAL] = SKY_LAYER
layer_map[LASEREAGLE | RED | WEBBED] = SKY_LAYER
layer_map[LASEREAGLE | RED | BURNING] = SKY_LAYER
layer_map[LASEREAGLE | BLUE | NORMAL] = SKY_LAYER
layer_map[LASEREAGLE | BLUE | WEBBED] = SKY_LAYER
layer_map[LASEREAGLE | BLUE | BURNING] = SKY_LAYER
layer_map[LASEREAGLE | YELLOW | NORMAL] = SKY_LAYER
layer_map[LASEREAGLE | YELLOW | WEBBED] = SKY_LAYER
layer_map[LASEREAGLE | YELLOW | BURNING] = SKY_LAYER
layer_map[LASEREAGLE | GREEN | NORMAL] = SKY_LAYER
layer_map[LASEREAGLE | GREEN | WEBBED] = SKY_LAYER
layer_map[LASEREAGLE | GREEN | BURNING] = SKY_LAYER

layer_map[BIGMAN | RED | NORMAL] = TROOP_LAYER
layer_map[BIGMAN | RED | WEBBED] = TROOP_LAYER
layer_map[BIGMAN | RED | BURNING] = TROOP_LAYER
layer_map[BIGMAN | BLUE | NORMAL] = TROOP_LAYER
layer_map[BIGMAN | BLUE | WEBBED] = TROOP_LAYER
layer_map[BIGMAN | BLUE | BURNING] = TROOP_LAYER
layer_map[BIGMAN | YELLOW | NORMAL] = TROOP_LAYER
layer_map[BIGMAN | YELLOW | WEBBED] = TROOP_LAYER
layer_map[BIGMAN | YELLOW | BURNING] = TROOP_LAYER
layer_map[BIGMAN | GREEN | NORMAL] = TROOP_LAYER
layer_map[BIGMAN | GREEN | WEBBED] = TROOP_LAYER
layer_map[BIGMAN | GREEN | BURNING] = TROOP_LAYER

layer_map[SPIDER | RED | NORMAL] = TROOP_LAYER
layer_map[SPIDER | RED | WEBBED] = TROOP_LAYER
layer_map[SPIDER | RED | BURNING] = TROOP_LAYER
layer_map[SPIDER | BLUE | NORMAL] = TROOP_LAYER
layer_map[SPIDER | BLUE | WEBBED] = TROOP_LAYER
layer_map[SPIDER | BLUE | BURNING] = TROOP_LAYER
layer_map[SPIDER | YELLOW | NORMAL] = TROOP_LAYER
layer_map[SPIDER | YELLOW | WEBBED] = TROOP_LAYER
layer_map[SPIDER | YELLOW | BURNING] = TROOP_LAYER
layer_map[SPIDER | GREEN | NORMAL] = TROOP_LAYER
layer_map[SPIDER | GREEN | WEBBED] = TROOP_LAYER
layer_map[SPIDER | GREEN | BURNING] = TROOP_LAYER

layer_map[BASE | RED | NORMAL] = BASE_LAYER
layer_map[BASE | RED | WEBBED] = BASE_LAYER
layer_map[BASE | RED | BURNING] = BASE_LAYER
layer_map[BASE | BLUE | NORMAL] = BASE_LAYER
layer_map[BASE | BLUE | WEBBED] = BASE_LAYER
layer_map[BASE | BLUE | BURNING] = BASE_LAYER
layer_map[BASE | YELLOW | NORMAL] = BASE_LAYER
layer_map[BASE | YELLOW | WEBBED] = BASE_LAYER
layer_map[BASE | YELLOW | BURNING] = BASE_LAYER
layer_map[BASE | GREEN | NORMAL] = BASE_LAYER
layer_map[BASE | GREEN | WEBBED] = BASE_LAYER
layer_map[BASE | GREEN | BURNING] = BASE_LAYER

layer_map[FLYINGTANK | RED | NORMAL] = SKY_LAYER
layer_map[FLYINGTANK | RED | WEBBED] = SKY_LAYER
layer_map[FLYINGTANK | RED | BURNING] = SKY_LAYER
layer_map[FLYINGTANK | BLUE | NORMAL] = SKY_LAYER
layer_map[FLYINGTANK | BLUE | WEBBED] = SKY_LAYER
layer_map[FLYINGTANK | BLUE | BURNING] = SKY_LAYER
layer_map[FLYINGTANK | YELLOW | NORMAL] = SKY_LAYER
layer_map[FLYINGTANK | YELLOW | WEBBED] = SKY_LAYER
layer_map[FLYINGTANK | YELLOW | BURNING] = SKY_LAYER
layer_map[FLYINGTANK | GREEN | NORMAL] = SKY_LAYER
layer_map[FLYINGTANK | GREEN | WEBBED] = SKY_LAYER
layer_map[FLYINGTANK | GREEN | BURNING] = SKY_LAYER

layer_map[CAR | RED | NORMAL] = TROOP_LAYER
layer_map[CAR | RED | WEBBED] = TROOP_LAYER
layer_map[CAR | RED | BURNING] = TROOP_LAYER
layer_map[CAR | BLUE | NORMAL] = TROOP_LAYER
layer_map[CAR | BLUE | WEBBED] = TROOP_LAYER
layer_map[CAR | BLUE | BURNING] = TROOP_LAYER
layer_map[CAR | YELLOW | NORMAL] = TROOP_LAYER
layer_map[CAR | YELLOW | WEBBED] = TROOP_LAYER
layer_map[CAR | YELLOW | BURNING] = TROOP_LAYER
layer_map[CAR | GREEN | NORMAL] = TROOP_LAYER
layer_map[CAR | GREEN | WEBBED] = TROOP_LAYER
layer_map[CAR | GREEN | BURNING] = TROOP_LAYER

layer_map[DRAGON | RED | NORMAL] = TROOP_LAYER
layer_map[DRAGON | RED | WEBBED] = TROOP_LAYER
layer_map[DRAGON | RED | BURNING] = TROOP_LAYER
layer_map[DRAGON | BLUE | NORMAL] = TROOP_LAYER
layer_map[DRAGON | BLUE | WEBBED] = TROOP_LAYER
layer_map[DRAGON | BLUE | BURNING] = TROOP_LAYER
layer_map[DRAGON | YELLOW | NORMAL] = TROOP_LAYER
layer_map[DRAGON | YELLOW | WEBBED] = TROOP_LAYER
layer_map[DRAGON | YELLOW | BURNING] = TROOP_LAYER
layer_map[DRAGON | GREEN | NORMAL] = TROOP_LAYER
layer_map[DRAGON | GREEN | WEBBED] = TROOP_LAYER
layer_map[DRAGON | GREEN | BURNING] = TROOP_LAYER

layer_map[LASER | RED] = TROOP_LAYER
layer_map[LASER | BLUE] = TROOP_LAYER
layer_map[LASER | YELLOW] = TROOP_LAYER
layer_map[LASER | GREEN] = TROOP_LAYER

layer_map[WEB | RED] = TROOP_LAYER
layer_map[WEB | BLUE] = TROOP_LAYER
layer_map[WEB | YELLOW] = TROOP_LAYER
layer_map[WEB | GREEN] = TROOP_LAYER

layer_map[FIREBALL | RED] = TROOP_LAYER
layer_map[FIREBALL | BLUE] = TROOP_LAYER
layer_map[FIREBALL | YELLOW] = TROOP_LAYER
layer_map[FIREBALL | GREEN] = TROOP_LAYER

layer_map[MISSILE | RED] = TROOP_LAYER
layer_map[MISSILE | BLUE] = TROOP_LAYER
layer_map[MISSILE | YELLOW] = TROOP_LAYER
layer_map[MISSILE | GREEN] = TROOP_LAYER

layer_map[SMALLMINERALPILE] = GROUND_LAYER
layer_map[MEDIUMMINERALPILE] = GROUND_LAYER
layer_map[LARGEMINERALPILE] = GROUND_LAYER

INVISIBLE = []
SMALL = [(0,0)]
MEDIUM = [(-1, -1), (0, -1), (-1, 0), (0, 0)]
LARGE = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
SMALL_PILE = []
for x in range(-2, 3):
    for y in range(-2, 3):
        SMALL_PILE.append((x, y))
MEDIUM_PILE = []
for x in range(-5, 5):
    for y in range(-5, 5):
        MEDIUM_PILE.append((x, y))
LARGE_PILE = []
for x in range(-7, 8):
    for y in range(-7, 8):
        LARGE_PILE.append((x, y))

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)

COLOR_GREY = (200, 200, 200)

icons: list[tuple[tuple[int,int,int], list[tuple[int,int]]]] = [(COLOR_RED, INVISIBLE)] * 1024

for t in [THREE, FOUR, MINER, MAN, LASEREAGLE]:
    for id, color in [(RED, COLOR_RED), (BLUE, COLOR_BLUE), (YELLOW, COLOR_YELLOW), (GREEN, COLOR_GREEN)]:
        for s in [NORMAL, WEBBED, BURNING, CARRYING]:
            icons[t | id | s] = color, SMALL

for t in [BIGMAN, SPIDER, FLYINGTANK, DRAGON]:
    for id, color in [(RED, COLOR_RED), (BLUE, COLOR_BLUE), (YELLOW, COLOR_YELLOW), (GREEN, COLOR_GREEN)]:
        for s in [NORMAL, WEBBED, BURNING, CARRYING]:
            icons[t | id | s] = color, MEDIUM

for t in [BASE, CAR]:
    for id, color in [(RED, COLOR_RED), (BLUE, COLOR_BLUE), (YELLOW, COLOR_YELLOW), (GREEN, COLOR_GREEN)]:
        for s in [NORMAL, WEBBED, BURNING, CARRYING]:
            icons[t | id | s] = color, LARGE

icons[SMALLMINERALPILE] = COLOR_GREY, SMALL_PILE
icons[MEDIUMMINERALPILE] = COLOR_GREY, MEDIUM_PILE
icons[LARGEMINERALPILE] = COLOR_GREY, LARGE_PILE
