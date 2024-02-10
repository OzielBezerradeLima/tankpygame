import pygame
import sys
import bomb
import game

playing = True


def close_screen():
    global playing
    playing = not playing


def map_create():

    pygame.init()
    WHITE = (255, 255, 255)