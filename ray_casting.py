import math

import pygame
from settings import *
from map import world_map


# def ray_casting(screen, player_position, player_angle):
#     cur_angle = player_angle - HALF_FOV
#     xo, yo = player_position
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#             # pygame.draw.line(screen, DARKGRAY, player_position, (x, y), 2)
#             if (x // TILE * TILE, y // TILE * TILE) in world_map:
#                 depth += math.cos(player_angle - cur_angle)
#                 proj_height = PROJ_COEFF / depth
#                 c = 255 / (1 + depth * depth * 0.00002)
#                 color = (c, c // 2, c // 2)
#                 pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
#                 break
#         cur_angle += DELTA_ANGEL

def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(screen, player_position, player_angle):
    ox, oy = player_position
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, dy + y) in world_map:
                break
            y += dy * TILE

        # projecting
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 2)
        pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGEL

        # if cos_a >= 0:
        #     x = xm + TILE
        #     dx = 1
        # else:
        #     x = xm
        #     dx = -1
