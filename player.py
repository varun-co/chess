from pieces import *
import pygame
class player:
    def find_match(self, obj, xpos, ypos):
        if obj.xpos == xpos and obj.ypos == ypos:
            return True

    def find_piece(self, xpos, ypos):
        for i in self.pawn_list:
            if self.find_match(i, xpos, ypos) and i.state == 'alive':
                return i
        for i in self.knight_list:
            if self.find_match(i, xpos, ypos) and i.state == 'alive':
                return i
        for i in self.bishop_list:
            if self.find_match(i, xpos, ypos) and i.state == 'alive':
                return i
        for i in self.rook_list:
            if self.find_match(i, xpos, ypos) and i.state == 'alive':
                return i
        for i in self.queen_list:
            if self.find_match(i, xpos, ypos) and i.state == 'alive':
                return i
        if self.find_match(self.king, xpos, ypos) and i.state == 'alive':
            return self.king
        return None

    def maker(self, i, screen):
        img = pygame.image.load(i.path)
        screen.blit(img, (i.xpos * 100 , i.ypos * 100))

    def destroyer(self):
        # to make all state to dead
        for i in self.pawn_list:
            i.state = 'dead'
        for i in self.knight_list:
            i.state = 'dead'
        for i in self.bishop_list:
            i.state = 'dead'
        for i in self.rook_list:
            i.state = 'dead'
        for i in self.queen_list:
            i.state = 'dead'
        self.king.state = 'dead'
    def draw_pieces(self, screen):
        for i in self.pawn_list:
            if i.state == 'alive':
                self.maker(i, screen)
        for i in self.knight_list:
            if i.state == 'alive':
                self.maker(i, screen)
        for i in self.bishop_list:
            if i.state == 'alive':
                self.maker(i, screen)
        for i in self.rook_list:
            if i.state == 'alive':
                self.maker(i, screen)
        for i in self.queen_list:
            if i.state == 'alive':
                self.maker(i, screen)
        self.maker(self.king, screen)


    def init_white(self):
        #initalising pawns
        self.pawn_list = []
        for i in range(8):
            self.pawn_list.append(pawn(i, 6, 'white'))
        #initalising rooks
        self.rook_list = []
        self.knight_list = []
        self.bishop_list = []
        self.queen_list = []
        for i in range(2):
            if i == 0:
                temp = rook(7, 7, 'white')
            else:
                temp = rook(0, 7, 'white')
            self.rook_list.append(temp)
        #initailsing knights
        for i in range(2):
            if i == 0:
                temp = knight(6, 7, 'white')
            else:
                temp = knight(1, 7, 'white')
            self.knight_list.append(temp)
        #intialising bishops
        for i in range(2):
            if i == 0:
                temp = bishop(2, 7, 'white')
            else:
                temp = bishop(5, 7, 'white')
            self.bishop_list.append(temp)
        #initalising queen
        self.queen_list = []
        for i in range(1):
            temp = queen(3, 7, 'white')
            self.queen_list.append(temp)
        #intialising king
        self.king = king(4, 7, 'white')

    def init_black(self):
        #initalising pawns
        self.pawn_list = []
        for i in range(8):
            self.pawn_list.append(pawn(i, 1, 'black'))
        #initalising rooks
        self.rook_list = []
        self.knight_list = []
        self.bishop_list = []
        self.queen_list = []
        for i in range(2):
            if i == 0:
                temp = rook(0, 0, 'black')
            else:
                temp = rook(7, 0, 'black')
            self.rook_list.append(temp)
        #initailsing knights
        for i in range(2):
            if i == 0:
                temp = knight(1, 0, 'black')
            else:
                temp = knight(6, 0, 'black')
            self.knight_list.append(temp)
        #intialising bishops
        for i in range(2):
            if i == 0:
                temp = bishop(2, 0, 'black')
            else:
                temp = bishop(5, 0, 'black')
            self.bishop_list.append(temp)
        #initalising queen
        self.queen_list = []
        for i in range(1):
            temp = queen(3, 0, 'black')
            self.queen_list.append(temp)
        #intialising king
        self.king = king(4, 0, 'black')

    def __init__(self, name, color):
        self.name = name
        self.color = color
        #intialising the intial position of the pieces
        if self.color == 'white':
            self.init_white()
        else:
            self.init_black()

