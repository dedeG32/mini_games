#unoptimized

from game import Game
import pygame
import random

class Sudoku(Game):
    def __init__(self):
        super().__init__()
        self.final_board = []
        self.genert_board()
        self.set_tick(3)
        self.font = self.set_font(font_size=30)

    def genert_board(self):
        line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(line)
        self.final_board.append(line)
        for loop1 in range(7):
            print(f"loop {loop1 +1 }")

            #while True:
            for loop2 in range(7):

                test = []
                line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(line)
                for index in range(len(self.final_board)):
                    for i in range(9):
                        test.append(line[i] == self.final_board[index][i])
                if not any(test) and len(self.final_board)+1 % 3 != 1:
                    case3x3_1 = [self.final_board[j][i] for i in range(3) for j in range(len(self.final_board)//3*3-1, len(self.final_board)//3*3+ len(self.final_board)-1, 1)]+ line[0:3]
                    case3x3_2 =[self.final_board[j][i] for i in range(3,6,1) for j in range(len(self.final_board)//3*3-1, len(self.final_board)//3*3+ len(self.final_board)-1, 1)]+ line[3:6]
                    case3x3_3 = [self.final_board[j][i] for i in range(6,9,1) for j in range(len(self.final_board)//3*3-1, len(self.final_board)//3*3+ len(self.final_board)-1, 1)]+ line[6:9]
                    if not len(set(case3x3_1)) == len(set(case3x3_2)) == len(set(case3x3_3))==6 or not len(set(case3x3_1)) == len(set(case3x3_2)) == len(set(case3x3_3))==9:
                        test.append(True)

                if not any(test):
                    self.final_board.append(line)
                    print(line)
                    break
        line = []
        for row in range(9):
            line += [i+1 for i in range(9) if i+1 not in [self.final_board[j][row] for j in range(8)] ]
        self.final_board.append(line)

    def set_screen_resolution(self):
        self.screen_width = self.screen_resolution[0] * 0.9 if self.screen_resolution[0] < self.screen_resolution[1] else self.screen_resolution[1] * 0.9
        self.screen_height = self.screen_width

    def solve(self):
        pass

    def display_game(self):
        print(self)
        self.screen.fill("white")

        #vertical lines
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width / 9, 0), (self.screen_width / 9, self.screen_height),1)
        pygame.draw.line(self.screen, (0, 0, 0), (2* self.screen_width / 9, 0), (2* self.screen_width / 9, self.screen_height),1)
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width / 3, 0), (self.screen_width / 3, self.screen_height),5)

        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width * 4 / 9, 0),(self.screen_width * 4 / 9, self.screen_height), 1)
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width * 5 / 9, 0),(self.screen_width * 5 / 9, self.screen_height), 1)
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width * 2 / 3, 0),(self.screen_width * 2 / 3, self.screen_height), 5)

        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width * 7 / 9, 0),(self.screen_width * 7 / 9, self.screen_height), 1)
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_width * 8 / 9, 0),(self.screen_width * 8 / 9, self.screen_height), 1)

        #horizontale lines
        for i in range(8):
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height *(i+1)/ 9), (self.screen_width, self.screen_height *(i+1)/ 9), 1)

        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height / 3), (self.screen_width, self.screen_height / 3),5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height * 2 / 3),(self.screen_width, self.screen_height * 2 / 3), 5)

        for j in range(9):
            for i in range(9):
                self.font.render_to(self.screen, (self.screen_width/18*(i*2+1) , self.screen_height/18*(j*2+1) ), str(self.final_board[j][i]), (0, 0, 0))

        pygame.display.flip()

    def enents(self):
        pass





    def __str__(self):
        string = ""
        for i in range(9):
            for j in range(17):
                if j%2 == 0:
                    string += str(self.final_board[i][j//2])
                else:
                    string += "\t|\t"

            string += "\n____________________________________________________________________\n"
        return string





if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.start()
