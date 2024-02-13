import pygame
import sys
import bomb
from codes import maze


playing = True


def create():
    maze.create_map("../maps/map1.txt")


def close_screen():
    global playing
    playing = not playing
