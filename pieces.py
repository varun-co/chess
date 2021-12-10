import os
class pieces:
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.state = 'alive'


class pawn(pieces):
    def draw(self):
        image = pygame.image.load('Icon/chess_board.png')

    def __init__(self, xpos, ypos, color):
        self.turn = 1
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'pawn.png')


class shadow(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', 'shadow.png')


class king(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'king.png')


class queen(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'queen.png')


class knight(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'knight.png')


class rook(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'rook.png')


class bishop(pieces):
    def __init__(self, xpos, ypos, color):
        super().__init__(xpos, ypos, color)
        self.path = os.path.join('Icon', color, 'bishop.png')
