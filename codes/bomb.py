import pygame
from main import screen


def create_bomb(bomb_info):
    pygame.draw.rect(screen, bomb_info['color'], [bomb_info['x'], bomb_info['y'], 10, 10])
    