import maze
import tank
import pygame
import sys
import settings


playing = True


def run():
    while playing:
        pygame.display.update()
        tank.controls(pygame.time.get_ticks())
        tank.bullet_move()
        tank.bullet_player_collision()
        tank.bullet_ricochet()
        tank.player_active()
        tank.draw_bullet()
        maze.draw_map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        maze.draw_map()


def close_screen():
    global playing
    playing = False
