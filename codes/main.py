import pygame
import sys
import game
import settings

pygame.init()
clock = pygame.time.Clock()
OPTIONS = ["Jogar", "Créditos", "Sair"]
CREDITS = ["Aglison Balieiro da Silva", "Felipe Alves Lopes", "Oziel Bezerra de Lima", " ", "Voltar"]
running = True
on_menu = True
selected = 0


def menu(selected_opt):
    settings.screen.fill(settings.WHITE)

    # Títulos
    title = settings.FONT.render("Tank Pygame", True, settings.BLACK)
    settings.screen.blit(title, (settings.WIDTH // 2 - title.get_width() // 2, 50))

    spacement = 50
    if on_menu:
        for i, option in enumerate(OPTIONS):
            # Define a cor do texto com base na seleção
            text_option = settings.FONT.render(option, True, settings.RED if i == selected_opt else settings.BLACK)

            # Posiciona o texto no centro da tela verticalmente
            position_x = settings.WIDTH // 2 - text_option.get_width() // 2
            position_y = 210 + i * spacement

            # Desenha o texto na tela
            settings.screen.blit(text_option, (position_x, position_y))
    else:
        for i, credit in enumerate(CREDITS):
            # Define a cor do texto com base na seleção
            text_option = settings.FONT.render(credit, True, settings.RED if i == 4 else settings.BLACK)

            # Posiciona o texto no centro da tela verticalmente
            position_x = settings.WIDTH // 2 - text_option.get_width() // 2
            position_y = 210 + i * spacement

            # Desenha o texto na tela
            settings.screen.blit(text_option, (position_x, position_y))


while running:
    if on_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.close_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    # Verifica qual opção foi selecionada e executa a ação correspondente
                    if selected == 0:
                        running = False
                        game.run()
                        print("Iniciar jogo!")
                    elif selected == 1:
                        print("Créditos")
                        on_menu = False
                    elif selected == 2:
                        pygame.quit()
                        sys.exit()
                # Movimenta a seleção para cima ou para baixo
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(OPTIONS)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(OPTIONS)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.close_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    on_menu = True

    menu(selected)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
