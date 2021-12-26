import pygame
import time
import os
from pieces import *
import pickle
import threading
from client import *
from player import *
class borad:
    def draw_borad(self, board_img):
        # to draw the borad
        self.screen.blit(board_img, (0,0))
    def update_pos(self):
        # to update the values of the objects depending on the chanes in state_table
        # first we make all piece dead
        self.player1.destroyer()
        self.player2.destroyer()

        for i in range(len(self.state_table)):
            for j in range(len(self.state_table[i])):
                temp = self.finder((i,j))
                piece = self.find_piece((i,j))
                if temp != None:
                    temp.state = 'alive'
                    temp.xpos = i
                    temp.ypos = j
    def translate(self):
        # to flip the state table
        self.state_table = [i[::-1] for i in self.state_table]

    def create_state_table(self):
        # to create the state table
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
        if self.player1.color== 'black':
            self.translate()
        self.update_pos()
    def generate_position(self, piece_obj, color):

        # to generate possible states of the foucs piecek
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
    def get_player(self,color):
        # get the player object where the color of the player is color
        if self.player1.color == color:
            return self.player1
        else:
            return self.player2

    def finder(self,pos):


        # will return object depeding upon what the value in the state table
        # position in pos
        if self.state_table[pos[0]][pos[1]] != '-':
            te = self.state_table[pos[0]][pos[1]]
            temp = None
            if te[0] == 'w':
                if self.player1.color == 'white':
                    te2 = self.player1
                else:
                    te2 = self.player2
                if te[1] == 'p':
                    temp = te2.pawn_list[int(te[2])]
                elif te[1] == 'r':
                    temp = te2.rook_list[int(te[2])]
                elif te[1] == 'k':
                    temp = te2.knight_list[int(te[2])]
                elif te[1] == 'b':
                    temp = te2.bishop_list[int(te[2])]
                elif te[1] == 'q':
                    temp = te2.queen_list[int(te[2])]
                elif te[1] == 'K':
                    temp = te2.king
            if te[0] == 'b':
                if self.player1.color == 'black':
                    te2 = self.player1
                else:
                    te2 = self.player2
                if te[1] == 'p':
                    temp = te2.pawn_list[int(te[2])]
                elif te[1] == 'r':
                    temp = te2.rook_list[int(te[2])]
                elif te[1] == 'k':
                    temp = te2.knight_list[int(te[2])]
                elif te[1] == 'b':
                    temp = te2.bishop_list[int(te[2])]
                elif te[1] == 'q':
                    temp = te2.queen_list[int(te[2])]
                elif te[1] == 'K':
                    temp = te2.king
            return temp
        return None
    def display(self):
        # to display the state table
        for i in self.state_table:
            print(*i)
    def find_piece(self, pos):
        # to find the piece in the state table at given position
        return self.state_table[pos[0]][pos[1]]
    def recvieve_state_table(self):

        # program for reciving the state table

        self.state_table = client_object.recv()
        self.state_table = pickle.loads(self.state_table)
        self.translate()
        self.turn = 1
    def __init__(self, player1, player2,opt):
        self.player1 = player1
        self.player2 = player2
        self.opt = opt
        self.focus_pos = None
        if self.player1.color == 'white':
            self.turn = 1
        else:
            self.turn = 2
        self.create_state_table()
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        running = True
        self.screen.fill((24, 34, 65))
        self.Icon = pygame.image.load(os.path.join('Icon', 'chess_logo.png'))
        pygame.display.set_icon(self.Icon)
        if self.player1.color == 'white':
            self.brd = pygame.image.load(os.path.join('Icon', 'chess_board.png'))
        else:
            self.brd = pygame.image.load(os.path.join('Icon', 'chess_board_1.png'))
        print(self.player1.color,self.player2.color)
        start = False
        while running:
            pos = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    pos = (pos[0] // 100), (pos[1] // 100)
                    break

            if self.turn == 1 and pos != None:
                piece = self.find_piece(pos)
                piece = self.state_table[pos[0]][pos[1]]
                if piece == '-' and self.focus_pos != None:
                    # logic for changing the state of
                    temp = self.find_piece(self.focus_pos)
                    self.state_table[self.focus_pos[0]][self.focus_pos[1]] = '-'
                    self.state_table[pos[0]][pos[1]] = temp
                    data_bytes = pickle.dumps(self.state_table)
                    client_object.send('send_to_server')
                    client_object.send(data_bytes)
                    self.turn = 2
                    self.focus_pos = None
                    start = False
                elif piece[0] == self.player2.color[0] and self.focus_pos != None:
                    # logic for capturing a piece
                    self.change_piece_state(pos)
                    temp = self.find_piece(self.focus_pos)
                    self.state_table[self.focus_pos[0]][self.focus_pos[1]] = '-'
                    self.state_table[pos[0]][pos[1]] = temp
                    data_bytes = pickle.dumps(self.state_table)
                    client_object.send('send_to_server')
                    client_object.send(data_bytes)
                    self.turn = 2
                    start = False
                    self.focus_pos = None

                elif piece[0] == self.player1.color[0]:
                    # logic for changing focus
                    self.focus_pos = pos

            elif self.turn == 2 and start == False:
                thread = threading.Thread(target=self.recvieve_state_table)
                thread.start()
                start = True



            self.update_pos()
            self.draw_borad(self.brd)
            self.player1.draw_pieces(self.screen)
            self.player2.draw_pieces(self.screen)
            pygame.display.update()


client_object = client_socket()
myname = input('Enter Player Name:')
print('[1]. For Creating New Game:')
print('[2]. For Joinning New Game:')
opt = int(input())
if opt == 1:
    code = generate_code()
    print('Enter The Below code in second player:')
    print(code)
    print('waiting for player to join...:')
elif opt ==2:
    print('Enter the code From the Host:')
    code = input()
msg = 'send_code_to_server'
client_object.send(msg)
client_object.send(code)
color = client_object.recv().decode(client_object.FORMAT)
print('Connection Established...')
if opt == 1:
    client_object.send('send_to_server')
    client_object.send(myname)
    opp_name = client_object.recv().decode(client_object.FORMAT)
elif opt == 2:
    opp_name = client_object.recv().decode(client_object.FORMAT)
    client_object.send('send_to_server')
    client_object.send(myname)
print(myname,opp_name)
print(f'Color of the player is {color}')
myself = player(myname,color)
if color == 'white':
    opponent = player(opp_name,'black')
else:
    opponent = player(opp_name,'white')
brd = borad(myself, opponent,opt)
client_object.disconect()
