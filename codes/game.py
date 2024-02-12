import pygame
import sys
import bomb

playing = True


def close_screen():
    global playing
    playing = not playing
