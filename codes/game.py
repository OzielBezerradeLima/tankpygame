from codes import maze
import pygame
import sys
import settings


playing = True


def run():
    maze.create_map()
    while playing:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def close_screen():
    global playing
    playing = False
