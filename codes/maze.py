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

    txt = "../assets/sand.jpeg"
    background_image = pygame.image.load(os.path.join(dirname, txt))
    dest = (0, 0)
    settings.screen.blit(background_image, dest)

    walls = []
    empty_spaces = []
    y = 0
    for lines in selected_map:
        x = 0
        for space in lines:
            if space == '1':
                walls.append(pygame.draw.rect(settings.screen, settings.WALL_COLOR, [x, y, 20, 20]))

            elif space == '0':
                empty_spaces.append([x, y])
            x += 20
        y += 20
    txt = "../assets/sand.jpeg"
    draw_map.background_image = pygame.image.load(os.path.join(dirname, txt))

    return walls, empty_spaces  # Retorna as paredes e espaços vazios


def draw_map():
    """Desenha o mapa continuamente na tela."""
    # Carrega o mapa aleatório se ainda não tiver sido carregado
    if not hasattr(draw_map, "walls"):
        draw_map.walls, draw_map.empty_spaces = create_map()

    block_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/wall_sprite.png"))

    # Desenha o fundo da tela
    settings.screen.blit(draw_map.background_image, (0, 0))

    for wall_rect in draw_map.walls:
        settings.screen.blit(block_image, wall_rect.topleft)

