class Chesspiece:
    def __init__(self, color: str, pos: tuple):
        self.color = color
        self.position = pos
        self.can_go_to = set()

    def __str__(self):
        return self.color[0] + type(self).__name__[0]

    def __add__(self, other):
        return other + self.color[0] + type(self).__name__[0]






class King(Chesspiece):
    def move_list(self, board):
        x = {(self.position[0]+j, self.position[1]+i) for i in range(-1,2, 1) for j in range(-1,2,1) if (self.position[0], self.position[1]) != (self.position[0]+j, self.position[1]+i) and board.available_case((self.position[0]+j, self.position[1]+i), self.color)}
        #x = {(self.position[0], self.position[1]) for i in range(8) if board.available_case((self.position[0] + 1, self.position[1] - 1 + i), self.color)}
        #print(x)

        return x

class Queen(Chesspiece):
    def move_list(self, board):
        self.can_go_to.clear()
        self.move_calculation(board, x=1)
        self.move_calculation(board, x=-1)
        self.move_calculation(board, y=1)
        self.move_calculation(board, y=-1)
        self.move_calculation(board, y=1  ,x=1)
        self.move_calculation(board, y=1 ,x=-1)
        self.move_calculation(board, y=-1  ,x=1)
        self.move_calculation(board, y=-1 ,x=-1)
        #print(self.can_go_to)
        return self.can_go_to

    def move_calculation(self, board, y=0, x=0):  # y controls the vertical movement, and x the horizontal
        i = 1
        while board.available_case((self.position[0] + y * i, self.position[1] + x * i), self.color):
            self.can_go_to.add((self.position[0] + y * i, self.position[1] + x * i))
            if board.occupied_case((self.position[0] + y * i, self.position[1] + x * i)): break
            i += 1

class Rook(Queen):
    def move_list(self, board):
        self.can_go_to.clear()
        self.move_calculation(board, x = 1)
        self.move_calculation(board, x = -1)
        self.move_calculation(board, y = 1)
        self.move_calculation(board, y = -1)
        #print(self.can_go_to)
        return self.can_go_to

    # def move_calculation(self, board, y =0 , x=0):  #y controls the vertical movement, and x the horizontal
    #     i = 1
    #     while board.available_case((self.position[0]+ y* i, self.position[1]+ x* i), self.color):
    #         self.can_go_to.add((self.position[0]+ y* i, self.position[1]+ x* i))
    #         if board.occupied_case((self.position[0]+ y* i, self.position[1]+ x* i)): break
    #         i += 1

class Bishop(Queen):
    def move_list(self, board):
        self.can_go_to.clear()
        self.move_calculation(board, y=1, x=1)
        self.move_calculation(board, y=1, x=-1)
        self.move_calculation(board, y=-1, x=1)
        self.move_calculation(board, y=-1, x=-1)
        #print(self.can_go_to)
        return self.can_go_to

class Nknight(Chesspiece): #######################
    def move_list(self, board):
        self.can_go_to = {(self.position[0] +i, self.position[1] +j) for i in range(-2, 3, 1) for j in range(-2, 3, 1) if i !=j and i != -j and i != 0 != j and board.available_case((self.position[0] +i, self.position[1] +j), self.color)}
        #print(self.can_go_to)
        return self.can_go_to


class Pawn(Chesspiece):
    #pos 1,0
    def move_list(self, board):
        up_down = 1 if self.color == "black" else -1  #variable making the pawn go down or up in the chessboard
        self.can_go_to = {(self.position[0] + 1 *up_down, self.position[1] - 1 + i) for i in range(3) if board.available_case((self.position[0] + 1 * up_down, self.position[1] - 1 + i), self.color if i != 1 else None, is_pawn=True)}
        #print(self.can_go_to)
        return self.can_go_to
    # def move_list(self, board):
    #     return {[self.position[0]+1, self.position[1]-1+i] for i in range(3) if board.availible_case([self.position[0]+1, self.position[1]-1+i], self.color if i != 1 else None)}







# list = [King('black',0) for _ in range(10)]
# print(" ".join([str(i) for i in list]))
#
# list[0].move()

