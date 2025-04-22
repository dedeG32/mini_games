import chess_pieces
class Chessboard:

    def __init__(self):
        self.board = [[ f"XX" for i in range(8)] for j in range(8)]
        self.win = False

    def game_loop(self):
        self.init_board()
        while not self.win:
            self.print_board()
            self.move_piece(input())


    def init_board(self):
        #set a and h row of the board (no king and queen)
        c = 'black'
        pos = 0
        for x in range(16):  # 12 nmb of pieces excluding king and queen
            if x ==8:
                c = 'white'
                pos = 7
            match x%8:
                case 0 | 7: self.board[pos][x%8] = chess_pieces.Rook(c, [pos, x % 8])
                case 1 | 6: self.board[pos][x%8] = chess_pieces.Nknight(c, [pos, x % 8])
                case 2 | 5: self.board[pos][x%8] = chess_pieces.Bishop(c, [pos, x % 8])
                case 3    : self.board[pos][x%8] = chess_pieces.King(c, [pos, x % 8])
                case 4    : self.board[pos][x%8] = chess_pieces.Queen(c, [pos, x % 8])

        #setting pawn placement
        for y in range(8):
            self.board[1][y] = chess_pieces.Pawn("black", [1, y])
        for y in range(8):
            self.board[6][y] = chess_pieces.Pawn("white", [7, y])


    def is_legit_case(self, pos):
        #check if case is out of list range
        return 0<=pos[0]<=7 and 0<=pos[1]<=7

    def occupied_case(self, pos):
        return self.board[pos[0]][pos[1]] != "XX"

    def available_case(self, pos ,color = None, is_pawn= False):
        if not self.is_legit_case(pos): return False

        if is_pawn:
            if color == None :   return self.board[pos[0]][pos[1]] == "XX"       # straight pawn True condition if case empty
            elif self.board[pos[0]][pos[1]] != "XX":                             #check if case not empty (pawn takes)
                return self.board[pos[0]][pos[1]].color != color
            else: return False



        elif self.board[pos[0]][pos[1]] == 'XX'  :  #case empty (avoid checking "XX".color)
            return True
        else: return self.board[pos[0]][pos[1]].color != color           #opposit color piece in the case


#possible improvement for available_case() : leave return self.board[pos[0]][pos[1]] == 'XX' as last line. and do smtg about pawn condition

    def illegale_move_message(self, pos):
        print("you can't go to this case")

    def player_turn(self, pos):
        if self.board[pos[0]][pos[1]].color == ("white" if self.player % 2 == 0 else "black"):
            return True
        else:
            print(("white" if self.player % 2 == 0 else "black"), ' turn')
            return False

    def move_piece(self, input_pos_to):
        pos, to = self.input_reader(input_pos_to.lower())
        if self.board[pos[0]][pos[1]] != "XX" and self.player_turn(pos):
            if to in self.board[pos[0]][pos[1]].move_list(self):
                self.board[to[0]][to[1]] = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = "XX"
                self.board[to[0]][to[1]].position = to
                self.player += 1
            else:
                print("you can't go to this case. Try again.")
                #raise NameError("you can't go to this case")

    def input_reader(self, input) -> ((int, int), (int, int)):
        #if len(input) == 5 and input[2] == " " and (input[1]+input[4]).isdigit() : # making sure the input is in the correct format "x1 y2"
        # The step is checked in valid input
        return ( ord(input[0])- 97, int(input[1]) -1 ),  ( ord(input[3])- 97, int(input[4]) -1 )

    def valid_input(self,input):
        if len(input) != 5 or input[2] != " " or not (input[1]+input[4]).isdigit():
            print('Incorrect format! try a format like "x9 x9"')

        elif input[:2] == input[3:]:
            print("You need to peek too distinct cases!")
        elif not 0<input[0]<9 or not 0<input[3]<9 and not 'a'<=input[1]<="h" and not 'a'<=input[4]<="h":
            print("please keep it between a/h and 1/8 ")
        else:
            return True
        return False

    def put_piece(self, piece):
        self.board[piece.position[0]][piece.position[1]] = piece


    def print_board(self):
        final = ''
        for i in range(16):

            if i % 2 == 1:
                final += "\t" + '-' * 41 + '\n'
            elif i % 2 == 0:
                final += chr(i // 2 + 97) + "   | " + " | ".join(str(i) for i in self.board[i // 2]) + " | \n"

        final += "\t  1    2    3    4    5    6    7    8 \n \n"#"\t " + ("\t" + "  ").join([str(j + 1) for j in range(8)])
        print(final)


if __name__ == "__main__":
    board = Chessboard()
    board.print_board()
    board.init_board()
    board.print_board()



