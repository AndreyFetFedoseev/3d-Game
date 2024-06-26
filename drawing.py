import pygame
from settings import *
from class_player import Player
from ray_casting import ray_casting
from map import mini_map


class Drawnig:

    def __init__(self, screen, map_screen):
        self.screen = screen
        self.map_screen = map_screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, SKY, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, POSITION_FPS)

    def mini_map(self, player):
        self.map_screen.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.line(self.map_screen, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                                   map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.map_screen, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.map_screen, GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.screen.blit(self.map_screen, POSITION_MAP)
