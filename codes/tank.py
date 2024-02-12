from bomb import create_bomb


class Tank:

    def __init__(self, player, color, x, y, direction):
        self.player = player
        self.bombs = []
        self.color = color
        self.x = x
        self.y = y
        self.direction = direction

    def movement(self, key):
        match key:
            case "W":
                match self.direction:
                    case 0:
                        self.y += 1
                    case 45:
                        self.x += 1
                        self.y += 1
                    case 90:
                        self.x += 1
                    case 135:
                        self.x += 1
                        self.y -= 1
                    case 180:
                        self.y -= 1
                    case 225:
                        self.x -= 1
                        self.y -= 1
                    case 270:
                        self.x -= 1
                    case 315:
                        self.x -= 1
                        self.y += 1

                print(self.player, "moved to [", self.x, ",", self.y, "]")
            case "A":
                self.direction -= 45
                if abs(self.direction) == 0:
                    self.direction = 315
                print(self.player, "turned to the left")
            case "D":
                self.direction += 45
                if abs(self.direction) == 360:
                    self.direction = 0
                print(self.player, "turned to the right")
            case "S":
                new_bomb = {'player': self.player, 'color': self.color, 'x': self.x, 'y': self.y,
                            'direction': self.direction, 'life_span': 5}
                self.bombs.append(create_bomb(new_bomb))
                print(self.player, "shot")

    def move_bombs(self):
        for bomb in self.bombs:
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
            self.bombs.remove(bomb)
