import pygame


# Tamanho da Tela e Cores
WIDTH, HEIGHT = 900, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializando tela e fonte
pygame.init()
FONT = pygame.font.Font(None, 42)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('COMBAT TANK')
