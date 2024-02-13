import pygame
import os


def create_map(txt):
    from main import screen
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, txt)
    selected_map = open(filename, 'r')
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
