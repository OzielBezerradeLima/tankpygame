import pygame


# Tamanho da Tela e Cores
WIDTH, HEIGHT = 900, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WALL_COLOR = (45, 75, 7)

# Cooldown dos tanks
ROTATE_COOLDOWN = 300
SHOOT_COOLDOWN = 300

# Inicializando tela e fonte
pygame.init()
FONT = pygame.font.Font(None, 42)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('COMBAT TANK')
