import os
import pygame
import sys

filename = sys.argv[1]

load = pygame.image.load(filename)
template = pygame.Surface(load.get_size(), flags=pygame.SRCALPHA)
template.blit(load, [0,0])
for x in range(template.get_size()[0]):
    for y in range(template.get_size()[1]):
        if template.get_at((x, y)) == (255, 255, 255, 255):
            template.set_at((x, y), pygame.color.Color(0, 0, 0, 0))

pygame.image.save(template, filename)
