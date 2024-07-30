import os
import pygame

PATH = "assets/graphics/elements/research"

COLORS = [
    ("blue", (0,0,255,255)),
    ("red", (255,0,0,255)),
    ("green", (0,255,0,255)),
    ("yellow", (255,255,0,255))
]

for filename in os.listdir(PATH):
    if filename.endswith(".png"):
        load = pygame.image.load(os.path.join(PATH, filename))
        template = pygame.Surface(load.get_size(), flags=pygame.SRCALPHA)
        template.blit(load, [0,0])
        for x in range(template.get_size()[0]):
            for y in range(template.get_size()[1]):
                if template.get_at((x, y)) == (255, 255, 255, 255):
                    template.set_at((x, y), pygame.color.Color(0, 0, 0, 0))

        name = filename.split(".")[0]
        effect = filename.split(".")[1]
        if not os.path.exists(os.path.join(PATH, name)):
            os.mkdir(os.path.join(PATH, name))
        for color, value in COLORS:
            for x in range(template.get_size()[0]):
                for y in range(template.get_size()[1]):
                    if load.get_at((x, y)) == (127,127,127,255) or load.get_at((x, y)) == (0,0,255,255):
                        template.set_at((x, y), value)
            if not os.path.exists(os.path.join(PATH, f"{name}/{color}")):
                os.mkdir(os.path.join(PATH, f"{name}/{color}"))
            pygame.image.save(template, os.path.join(PATH, f"{name}/{color}/{effect}.png"))

