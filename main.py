import pygame

from ray_casting import ray_casting
from settings import *
from class_player import Player
from drawing import Drawnig
import math
from map import world_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
map_screen = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawnig(screen, map_screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        player.movement()
        screen.fill(BLACK)

        drawing.background()
        drawing.world(player.position, player.angle)
        drawing.fps(clock)
        drawing.mini_map(player)
        # ray_casting(screen, player.position, player.angle)



        pygame.display.flip()
        clock.tick()
