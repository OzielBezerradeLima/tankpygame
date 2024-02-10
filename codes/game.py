import pygame
import sys
import bomb
import game

playing = True


def close_screen():
    global playing
    playing = not playing
