import maze
import tank
import pygame
import sys
import settings


playing = True


def run():
    maze.create_map()
    while playing:
        pygame.display.update()
        tank.controls(pygame.time.get_ticks())
        tank.bullet_move()
        tank.bullet_player_collision()
        tank.bullet_ricochet()
        tank.player_active()
        tank.draw_bullet()



def close_screen():
    global playing
    playing = False
