import pygame


def create_bomb(bomb_info):
    from main import screen
    pygame.draw.rect(screen, bomb_info['color'], [bomb_info['x'], bomb_info['y'], 10, 10])


def move_bombs(bombs):
    for bomb in bombs:
        while bomb['life_span'] > 0:
            match bomb['direction']:
                case 0:
                    bomb['x'] += 1
                case 45:
                    bomb['x'] += 1
                    bomb['y'] += 1
                case 90:
                    bomb['x'] += 1
                case 135:
                    bomb['x'] += 1
                    bomb['y'] -= 1
                case 180:
                    bomb['y'] -= 1
                case 225:
                    bomb['x'] -= 1
                    bomb['y'] -= 1
                case 270:
                    bomb['x'] -= 1
                case 315:
                    bomb['x'] -= 1
                    bomb['y'] += 1
            bomb['life_span'] -= 1
            print("Position of bomb shot by ", bomb['player'], " [", bomb['x'], ", ", bomb['y'], "]")
        bombs.remove(bomb)
