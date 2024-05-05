import pygame

from ray_casting import ray_casting
from settings import *
from class_player import Player
import math
from map import world_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        player.movement()
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

        ray_casting(screen, player.position, player.angle)

        # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 15)
        # pygame.draw.line(screen, GREEN, player.position, (player.x + WIDTH * math.cos(player.angle),
        #                                                   player.y + WIDTH * math.sin(player.angle)))
        # for x, y in world_map:
        #     pygame.draw.rect(screen, WHITE, (x, y, TILE, TILE), 2)

        pygame.display.flip()
        clock.tick(FPS)
