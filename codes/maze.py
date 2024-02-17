import pygame
import os
import settings
import random


def create_map():
    random_choice = str(random.randint(1, 5))
    txt = "../maps/map"+random_choice+".txt"
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, txt)
    selected_map = open(filename, 'r')

    settings.screen.fill([0, 0, 0])
    walls = []
    empty_spaces = []
    y = 0
    for lines in selected_map:
        x = 0
        for space in lines:
            if space == '1':
                walls.append(pygame.draw.rect(settings.screen, (255, 255, 255), [x, y, 20, 20]))
            elif space == '0':
                empty_spaces.append([x, y])
            x += 20
        y += 20
