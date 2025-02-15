from game import Game
import pygame
import time

#Class________________________________________________________
class Tic_tac_toe2(Game):
    def __init__(self):
        super().__init__()
        self.board = [["." for _ in range(3)] for _ in range(3)]
        self.player = 1
        self.set_tick(3)
        self.font = self.set_font(font_size= 30)

    def display_game(self):
        self.screen.fill("white")
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


    def add_to_board(self):
        self.click_y_index, self.click_x_index = self.indexing_pos()
        if self.board[self.click_y_index][self.click_x_index] == ".":
            self.board[self.click_y_index][self.click_x_index] = "O" if self.player %2 ==0 else "X"
            self.player += 1
        else:
            print("can't do that!")

    def set_screen_resolution(self):
        self.screen_width = self.screen_resolution[0] * 0.7 if self.screen_resolution[0]<self.screen_resolution[1] else self.screen_resolution[1] *0.7
        self.screen_height = self.screen_width
    def click_on_screen(self, click_pos):
        self.click_x,self.click_y = click_pos
        return 0<self.click_x<self.screen_width and 0<self.click_y<self.screen_height

    def indexing_pos(self):
         return  int(self.click_y/self.screen_height*3), int(self.click_x/self.screen_width*3)

    def align_3(self):
        if self.board[self.click_y_index][0] == self.board[self.click_y_index][1] == self.board[self.click_y_index][2] != ".":
            self.final_line = (self.click_y_index, 0), (self.click_y_index, 2)
            return True

        elif self.board[0][self.click_x_index] == self.board[1][self.click_x_index] == self.board[2][self.click_x_index] != '.':
            self.final_line = (0, self.click_x_index), (2, self.click_x_index)
            return True

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '.':
            self.final_line = (0, 0), (2, 2)
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ".":
            self.final_line = (0, 2), (2, 0)
            return True

    def index_to_coordinate(self):
        pass

    # def align_3(self):
    #         return (self.board[self.click_y_index][0] == self.board[self.click_y_index][1] ==self.board[self.click_y_index][2] != ".") or (self.board[0][self.click_x_index] == self.board[1][self.click_x_index] == self.board[2][self.click_x_index] != '.') or (self.board[0][0] == self.board[1][1] == self.board[2][2] != '.') or (self.board[0][2] == self.board[1][1] == self.board[2][0] != ".")

    def check_win(self):
        if self.player > 5 and self.align_3():
            print(f'player {self.player % 2 + 1} won')
            pygame.draw.line(self.screen, (250, 0, 0), ((self.final_line[0][1] *2+1 )* self.screen_width/6, (self.final_line[0][0]*2+1)*self.screen_height/6),((self.final_line[1][1]*2+1)* self.screen_width/6, (self.final_line[1][0]*2+1)*self.screen_height/6), 8)
            self.font.render_to(self.screen, (self.screen_width/2 -110, self.screen_height/2-10), f'PLAYER {self.player % 2 + 1} WON', (0, 255, 0))
            pygame.display.flip()
            time.sleep(5)
            self.win = True

    def events(self, event) -> None:
        if pygame.mouse.get_pressed()[0] and self.click_on_screen(pygame.mouse.get_pos()):
            self.add_to_board()



###############################################################################################
#_____________________________________________________________________________________________


if __name__ == "__main__":
    screen_size = ()  # (1280, 720)
    # pygame setup

    game = Tic_tac_toe2()

    game.start()



