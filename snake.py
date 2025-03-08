from game import Game
from menu import get_int
import pygame

class Snake(Game):
    class Node:
        def __init__(self, pos_y, pos_x, next= None):
            """
            :param next: next node of the snake
            :param position: (y,x) : pos y first then x
            """
            self.next = next
            self.pos_y :int  = pos_y
            self.pos_x :int = pos_x

        def next(self):
            return self.next
        # def next(self):
        #     self.pos_y = self.next.position[0]
        #     self.pos_x = self.next.position[1]
        #     self.next = self.next.next


    def __init__(self):
        super().__init__()
        #board
        self.board_size = self.ask_board_size()
        self.board = [["_" for _ in range(self.board_size)] for _ in range(self.board_size)]
        print(self.board)
        self.display_cell = self.screen_width//self.board_size
        #===========================================================
        #snake_player
        self.head = self.Node(self.board_size // 2 , self.board_size // 2 -1)
        self.tail = self.Node(self.board_size // 2 , self.board_size // 2 -2, self.head)
        self.snake_size = 1
        self.direction = 1 # no movement

    def ask_board_size(self):
        print("Please enter the size of the board (5-100): ")
        return get_int(5,100)

    def display_game(self):
        self.screen.fill("white")
        for row in range(self.board_size):
            for i in range(self.board_size):
                pygame.draw.rect(self.screen, "black", pygame.Rect(i * self.display_cell, row * self.display_cell, self.display_cell, self.display_cell ))

        pygame.draw.line(self.screen,(0,0,0), (self.screen_width/3, 0), (self.screen_width/3, self.screen_height), 5 )
        pygame.draw.line(self.screen,(0,0,0), (self.screen_width*2 /3, 0), (self.screen_width*2/3, self.screen_height), 5 )
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height /3), (self.screen_width, self.screen_height/3), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height*2 /3), (self.screen_width , self.screen_height*2/3), 5)
        for y_dex, i in enumerate(self.board):
            for x_dex, j in enumerate(i):
                if j == "X":#########################################################################################3333333333333
                    pygame.draw.line(self.screen, (0,0,0), ((x_dex*4+1)*self.screen_width/12, (y_dex*4+1)*self.screen_height/12), (((x_dex*4)+3)*self.screen_width/12,((y_dex*4)+3)*self.screen_height/12),5)
                    pygame.draw.line(self.screen, (0, 0, 0), ((x_dex*4+1)*self.screen_width / 12, ((y_dex*4)+3)*self.screen_height/12),(((x_dex*4)+3)* self.screen_width / 12, (y_dex*4+1)*self.screen_height/12),5)
                elif j == "O":
                    pygame.draw.circle(self.screen, (0,0,0), ((x_dex*2+1)*self.screen_width/6, (y_dex*2+1)*self.screen_height/6), self.screen_height/9, 5)
        self.set_tick(2)

    def snake_move(self):
        """
        Move the snake and refresh board
        :return:
        """
        print(0 >= self.head.pos_x + self.direction // 2 >= self.board_size -1, "0>=",self.head.pos_x + self.direction // 2, ">= " ,self.board_size -1)
        if self.direction % 2 ==0:
            if 0 >= self.head.pos_x + self.direction // 2 or self.head.pos_x + self.direction // 2 >= self.board_size -1 :
                self.win = True
                return

            if self.board[self.head.pos_y][self.head.pos_x + self.direction // 2] == "1":   #food on the next case
                self.head.next = self.Node(self.head.pos_y, self.head.pos_x + self.direction // 2)
                self.head = self.head.next
                self.snake_size += 1
            else:
                self.head.next = self.Node(self.head.pos_y, self.head.pos_x + self.direction // 2)
                self.head = self.head.next
                self.tail = self.tail.next
        elif self.direction % 3 ==0:
            if 0 >= self.head.pos_y + self.direction // 3 or self.head.pos_y + self.direction // 3 >= self.board_size -1:
                self.win = True
                return

            if self.board[self.head.pos_y + self.direction // 3][self.head.pos_x ] == "1":  # food on the next case
                self.head.next = self.Node(self.head.pos_y + self.direction // 3 , self.head.pos_x)
                self.head = self.head.next
                self.snake_size += 1
            else:
                self.head.next = self.Node(self.head.pos_y + self.direction // 3, self.head.pos_x)
                self.head = self.head.next
                self.board[self.tail.pos_y][self.tail.pos_x] = "_"
                self.tail = self.tail.next

        if (self.board[self.head.pos_y-1][self.head.pos_x-1] == "0" and self.direction !=1) :
            self.win = True
        else:
            self.board[self.head.pos_y][self.head.pos_x] = "0"


    def refresh_board(self):
        node = self.tail

        for i in range(self.snake_size):
            self.board[node.pos_y][node.pos_x] = "0"


    def spawn_food(self):
        pass

    def set_screen_resolution(self):
        self.screen_width = self.screen_resolution[0] * 0.9 if self.screen_resolution[0]<self.screen_resolution[1] else self.screen_resolution[1] *0.9
        self.screen_height = self.screen_width


    def action(self) -> None:
        self.snake_move()
        print(self)


    def __repr__(self):
        string = ""
        for row in self.board:
            string += str(row) + "\n"
        string += "\n"
        return string

if __name__ == "__main__":
    game = Snake()
    game.start()