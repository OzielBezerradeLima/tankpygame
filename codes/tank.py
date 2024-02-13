from bomb import create_bomb, move_bombs


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
        move_bombs(self.bombs)
