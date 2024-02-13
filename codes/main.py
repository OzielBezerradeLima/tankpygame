import pygame
import sys
import bomb
import game

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
FONT = pygame.font.Font(None, 42)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('COMBAT TANK')
clock = pygame.time.Clock()
options = ["Jogar", "Créditos", "Sair"]

def menu(selected):
    screen.fill(WHITE)

    # Títulos
    title = FONT.render("Tank Pygame", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    spacement = 50

    for i, option in enumerate(options):
        # Define a cor do texto com base na seleção
        text_option = FONT.render(option, True, RED if i == selected else BLACK)

        # Posiciona o texto no centro da tela verticalmente
        position_x = WIDTH // 2 - text_option.get_width() // 2
        position_y = 210 + i * spacement

        # Desenha o texto na tela
        screen.blit(text_option, (position_x, position_y))

selected = 0
while game.playing:
    screen.fill((BLACK))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.close_screen()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.key == pygame.K_RETURN:
            # Verifica qual opção foi selecionada e executa a ação correspondente
            if selecionado == 0:
                print("Iniciar jogo!")
            elif selecionado == 1:
                print("Créditos")
            elif selecionado == 2:
                pygame.quit()
                sys.exit()

        # Movimenta a seleção para cima ou para baixo
        if event.key == pygame.K_UP:
            selected = (selected - 1) % len(options)
        elif event.key == pygame.K_DOWN:
            selected = (selected + 1) % len(options)

    menu(selected)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
