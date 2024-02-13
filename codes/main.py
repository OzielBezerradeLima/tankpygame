import pygame
import sys
import game

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('COMBAT TANK')
clock = pygame.time.Clock()
game.create()

while game.playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.close_screen()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
