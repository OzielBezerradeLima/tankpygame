import pygame
from main import screen


def create_map(txt):
    selected_map = (txt, "r")
    walls = []
    empty_spaces = []

    y = 0
    for lines in selected_map:
        x = 0
        for space in lines:
            if space == '1':
                walls.append(pygame.draw.rect(screen, [255, 255, 255], [x, y, 10, 10]))
            elif space == '0':
                empty_spaces.append([x, y])
            x += 10
        y += 10
