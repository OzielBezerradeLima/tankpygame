import pygame
import settings
import os


class Player:
    def __init__(self, image_path, bullet_image_path, starting_position, controls, last_rotate_time, last_shoot_time):
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rotation_center = self.rect.center
        self.position = starting_position
        self.speed = 5
        self.rotation_angle = 0
        self.lives = 3
        self.active = True
        self.controls = controls
        self.last_rotate_time = last_rotate_time
        self.last_shoot_time = last_shoot_time

    def rotate(self, angle):
        if self.active:
            self.rotation_angle += angle

    def move(self):
        if self.active:
            self.position += pygame.math.Vector2(0, -self.speed).rotate(-self.rotation_angle)
            self.position.x %= settings.WIDTH
            self.position.y %= settings.HEIGHT

    def shoot(self):
        if self.active:
            bullet_speed = 7
            bullet_direction = pygame.math.Vector2(0, -bullet_speed).rotate(-self.rotation_angle)
            bullet_position_front = self.position + pygame.math.Vector2(self.rect.width / 2, 0).rotate(
                -self.rotation_angle)
            return {'id': f'player_{self.controls["shoot"]}', 'position': bullet_position_front,
                    'direction': bullet_direction, 'life': 60}

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        self.rect = rotated_image.get_rect(center=self.rotation_center)
        screen.blit(rotated_image, self.position - pygame.math.Vector2(self.rect.width / 2, self.rect.height / 2))


# Função para verificar a colisão entre dois retângulos
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


# Define o diretório do arquivo
dirname = os.path.dirname(__file__)

# Crie instâncias da classe Player
player1_controls = {'rotate_left': pygame.K_LEFT, 'rotate_right': pygame.K_RIGHT, 'move_forward': pygame.K_UP,
                    'shoot': pygame.K_SPACE}
player1_sprite = os.path.join(dirname, "../assets/tank_sprite2.png")
player1 = Player(player1_sprite, "",
                 pygame.math.Vector2(settings.WIDTH / 4, settings.HEIGHT / 2), player1_controls, 0, 0)

player2_controls = {'rotate_left': pygame.K_a, 'rotate_right': pygame.K_d, 'move_forward': pygame.K_w,
                    'shoot': pygame.K_TAB}
player2_sprite = (os.path.join(dirname, "../assets/tank2_sprite2.png"))
player2 = Player(player2_sprite, "",
                 pygame.math.Vector2(3 * settings.WIDTH / 4, settings.HEIGHT / 2), player2_controls, 0, 0)

# Defina a lista de balas
bullets = []

bullet_image_path = "../assets/bullet_sprite.png"
bullet_image = pygame.image.load(bullet_image_path)


def controls(now):
    # Verifique os eventos de teclado para o jogador 1
    keys = pygame.key.get_pressed()
    if keys[player1.controls['rotate_left']]:
        if now - player1.last_rotate_time >= settings.ROTATE_COOLDOWN:
            player1.last_rotate_time = pygame.time.get_ticks()
            player1.rotate(45)
    if keys[player1.controls['rotate_right']]:
        if now - player1.last_rotate_time >= settings.ROTATE_COOLDOWN:
            player1.last_rotate_time = pygame.time.get_ticks()
            player1.rotate(-45)
    if keys[player1.controls['move_forward']]:
        player1.move()
    if keys[player1.controls['shoot']]:
        if now - player1.last_shoot_time >= settings.SHOOT_COOLDOWN:
            player1.last_shoot_time = pygame.time.get_ticks()
            bullet = player1.shoot()
            bullets.append(bullet)

    # Verifique os eventos de teclado para o jogador 1
    if keys[player2.controls['rotate_left']]:
        if now - player2.last_rotate_time >= settings.ROTATE_COOLDOWN:
            player2.last_rotate_time = pygame.time.get_ticks()
            player2.rotate(45)
    if keys[player2.controls['rotate_right']]:
        if now - player2.last_rotate_time >= settings.SHOOT_COOLDOWN:
            player2.last_rotate_time = pygame.time.get_ticks()
            player2.rotate(-45)
    if keys[player2.controls['move_forward']]:
        player2.move()
    if keys[player2.controls['shoot']]:
        if now - player2.last_shoot_time >= settings.SHOOT_COOLDOWN:
            player2.last_shoot_time = pygame.time.get_ticks()
            bullet = player2.shoot()
            bullets.append(bullet)


def bullet_move():
    # Atualize as posições e tempos de vida das balas
    for bullet in bullets:
        bullet['position'] += bullet['direction']
        bullet['life'] -= 1
        if bullet['life'] <= 0:
            bullets.remove(bullet)


def bullet_player_collision():
    # Verifique a colisão entre jogadores e balas
    global bullets
    for player in [player1, player2]:
        if player.active:
            player_rect = player.rect.move(player.position.x - player.rect.width / 2,
                                           player.position.y - player.rect.height / 2)
            for bullet in bullets:
                bullet_rect = pygame.Rect(bullet['position'].x - bullet_image.get_width() / 2,
                                          bullet['position'].y - bullet_image.get_height() / 2,
                                          bullet_image.get_width(),
                                          bullet_image.get_height())

                # Verifique a colisão apenas se o identificador da bala for diferente do identificador do jogador
                if bullet['id'] != f'player_{player.controls["shoot"]}' and check_collision(player_rect, bullet_rect):
                    player.lives -= 1
                    bullets.remove(bullet)
                    print(f"O jogador {player.controls['shoot']} foi atingido! Vidas restantes: {player.lives}")

                    if player.lives == 0:
                        print(f"Game Over! Jogador {player.controls['shoot']} derrotado!")
                        player.active = False
                        player.lives = 3
                        player.position = pygame.math.Vector2(
                            settings.WIDTH / 4 if player.controls['shoot'] == pygame.K_SPACE else 3 * settings.WIDTH / 4, settings.HEIGHT / 2)
                        bullets = []


def bullet_ricochet():
    # Verifique se a bala atingiu as bordas da tela e aplique a mecânica de ricochete
    for bullet in bullets:
        if not (0 <= bullet['position'].x <= settings.WIDTH and 0 <= bullet['position'].y <= settings.HEIGHT):
            bullet['direction'] = -bullet['direction']


def player_active():
    # Desenhe os jogadores apenas se estiverem ativos
    if player1.active:
        player1.draw(settings.screen)
    if player2.active:
        player2.draw(settings.screen)


def draw_bullet():
    # Desenhe as balas na tela
    for bullet in bullets:
        settings.screen.blit(bullet_image, bullet['position'] - pygame.math.Vector2(bullet_image.get_width() / 2,
                             bullet_image.get_height() / 2))
    pygame.display.flip()
