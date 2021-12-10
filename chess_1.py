import pygame
import os
from pieces import *
import pickle
from client import *
class borad:
    def draw_borad(self, board_img):
        self.screen.blit(board_img, (100, 100))
    def create_state_table(self):
        self.state_table = [['-' for i in range(8)] for j in range(8)]
        self.state_table[0][0] = 'br0'
        self.state_table[1][0] = 'bk0'
        self.state_table[2][0] = 'bb0'
        self.state_table[3][0] = 'bq0'
        self.state_table[4][0] = 'bK0'
        self.state_table[5][0] = 'bb1'
        self.state_table[6][0] = 'bk1'
        self.state_table[7][0] = 'br1'
        self.state_table[0][1] = 'bp0'
        self.state_table[1][1] = 'bp1'
        self.state_table[2][1] = 'bp2'
        self.state_table[3][1] = 'bp3'
        self.state_table[4][1] = 'bp4'
        self.state_table[5][1] = 'bp5'
        self.state_table[6][1] = 'bp6'
        self.state_table[7][1] = 'bp7'
        self.state_table[0][7] = 'wr0'
        self.state_table[1][7] = 'wk0'
        self.state_table[2][7] = 'wb0'
        self.state_table[3][7] = 'wq0'
        self.state_table[4][7] = 'wK0'
        self.state_table[5][7] = 'wb1'
        self.state_table[6][7] = 'wk1'
        self.state_table[7][7] = 'wr1'
        self.state_table[0][6] = 'wp0'
        self.state_table[1][6] = 'wp1'
        self.state_table[2][6] = 'wp2'
        self.state_table[3][6] = 'wp3'
        self.state_table[4][6] = 'wp4'
        self.state_table[5][6] = 'wp5'
        self.state_table[6][6] = 'wp6'
        self.state_table[7][6] = 'wp7'

    def generate_position(self, piece_obj, color):
        possible_pos = []
        if type(piece_obj).__name__ == 'pawn':
            if piece_obj.turn == 1 and color == 'white':
                possible_pos.append(pos[0], pos[1] - 1)
                possible_pos.append(pos[0], pos[1] - 2)
                piece_obj.turn = 0
            elif piece_obj.turn == 1 and color == 'black':
                possible_pos.append(pos[0], pos[1] + 1)
                possible_pos.append(pos[0], pos[1] + 2)
                piece_obj.turn = 0
            elif color == 'white':
                possible_pos.append(pos[0], pos[1] - 1)
            elif color == 'black':
                possible_pos.append(pos[0], pos[1] + 1)
        return possible_pos

    def find_piece(self, pos, turn):
        color = 1
        if turn == 1:
            color = self.player1.color
        else:
            color = self.player2.color

        if self.state_table[pos[0]][pos[1]] != '-':
            te = self.state_table[pos[0]][pos[1]]
            temp = None
            if te[0] == 'w' and color == 'white':
                if te[1] == 'p':
                    temp = self.player1.pawn_list[int(te[2])]
                elif te[1] == 'r':
                    temp = self.player1.rook_list[int(te[2])]
                elif te[1] == 'k':
                    temp = self.player1.knight_list[int(te[2])]
                elif te[1] == 'b':
                    temp = self.player1.bishop_list[int(te[2])]
                elif te[1] == 'q':
                    temp = self.player1.queen_list[int(te[2])]
                elif te[1] == 'K':
                    temp = self.player1.king
            if te[0] == 'b' and color == 'black':
                if te[1] == 'p':
                    temp = self.player2.pawn_list[int(te[2])]
                elif te[1] == 'r':
                    temp = self.player2.rook_list[int(te[2])]
                elif te[1] == 'k':
                    temp = self.player2.knight_list[int(te[2])]
                elif te[1] == 'b':
                    temp = self.player2.bishop_list[int(te[2])]
                elif te[1] == 'q':
                    temp = self.player2.queen_list[int(te[2])]
                elif te[1] == 'K':
                    temp = self.player2.king
            return temp
        return temp

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.focus_piece = None
        if self.player1.color == 'white':
            self.turn = 1
        else:
            self.turn = 2
        self.create_state_table()
        running = True
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))
        running = True
        self.screen.fill((24, 34, 65))
        self.Icon = pygame.image.load(os.path.join('Icon', 'chess_logo.png'))
        pygame.display.set_icon(self.Icon)
        self.brd = pygame.image.load(os.path.join('Icon', 'chess_board.png'))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    pos = (pos[0] // 100) - 1, (pos[1] // 100) - 1
                    if self.turn == 1:
                        if self.state_table[pos[0]][pos[1]] != '-':
                            self.focus_piece = self.find_piece(pos, 1)
                        else:
                            if self.focus_piece != None:
                                self.focus_piece.xpos = pos[0]
                                self.focus_piece.ypos = pos[1]
                                self.turn = 2
                                self.focus_piece = None
                        '''temp = player1.find_piece(pos[0], pos[1])
                        if temp == None and self.focus_piece != None:
                            temp2 = player2.find_piece(pos[0], pos[1])
                            if temp2 != None:
                                temp2.state = 'dead'
                            self.focus_piece.xpos = pos[0]
                            self.focus_piece.ypos = pos[1]
                            self.turn = 2
                            self.focus_piece = None
                        self.focus_piece = temp
                        self.generate_position(temp)'''
                    else:
                        if self.state_table[pos[0]][pos[1]] != '-':
                            self.focus_piece = self.find_piece(pos, 2)
                        else:
                            if self.focus_piece != None:
                                self.focus_piece.xpos = pos[0]
                                self.focus_piece.ypos = pos[1]
                                self.turn = 1
                                self.focus_piece = None
                        '''temp = player2.find_piece(pos[0], pos[1])
                        if temp == None and self.focus_piece != None:
                            temp2 = player1.find_piece(pos[0], pos[1])
                            if temp2 != None:
                                temp2.state = 'dead'
                            self.focus_piece.xpos = pos[0]
                            self.focus_piece.ypos = pos[1]
                            self.turn = 1
                            self.focus_piece = None
                        self.focus_piece = temp'''
                self.draw_borad(self.brd)
            player1.draw_pieces(self.screen)
            player2.draw_pieces(self.screen)
            pygame.display.update()


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
        screen.blit(img, (i.xpos * 100 + 100, i.ypos * 100 + 100))

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


#inititalise pygame
p1 = player('varun', 'white')
p2 = player('kudi', 'black')
client_object = client_socket()
print('[1]. For Creating New Game')
print('[2]. For Joinning New Game')
opt = int(input())
if opt == 1:
    code = generate_code()
    print('Enter The Below code in second player')
    print(code)
    print('waiting for player to join...')
elif opt ==2:
    print('Enter the code From the Host')
    code = input()
msg = 'send_code_to_server'.encode(client_object.FORMAT)
client_object.send(msg)
client_object.send(code)
print('Connection Established...')
#if opt == 2:
    #n = int(input('Enter the No of inputs'))
    #lt = []
    #for i in range(n):
        #temp = input()
        #lt.append(temp)
    #msg = pickle.dumps(lt)
    #mode = 'list_send_to_server'.encode(client_object.FORMAT)
    #client_object.send(mode)
    #client_object.send(msg)
#elif opt == 3:
    #msg = client_object.recv()
    #msg = pickle.loads(msg)
    #print(msg)
#brd = borad(p1, p2)
