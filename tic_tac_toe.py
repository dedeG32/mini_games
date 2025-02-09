import time

import pygame

#Class________________________________________________________
class Tic_tac_toe():
    def __init__(self, screen_resolution):#, surface):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        clock = pygame.time.Clock()
        clock.tick(10)  # limits FPS to 10
        self.board = [["." for _ in range(3)] for _ in range(3)]
        self.player = 1
        # # self.board[1][1] = "O"
        # # self.board[2][1] = "O"
        # self.board[0][1] = "X"
        self.win = False
        #self.surface = surface
        self.screen_width, self.screen_high = screen_resolution


    def display_board(self):
        self.screen.fill("white")
        pygame.draw.line(self.screen,(0,0,0), (self.screen_width/3, 0), (self.screen_width/3, self.screen_high), 5 )
        pygame.draw.line(self.screen,(0,0,0), (self.screen_width*2 /3, 0), (self.screen_width*2/3, self.screen_high), 5 )
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_high /3), (self.screen_width, self.screen_high/3), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_high*2 /3), (self.screen_width , self.screen_high*2/3), 5)
        for y_dex, i in enumerate(self.board):
            for x_dex, j in enumerate(i):
                if j == "X":#########################################################################################3333333333333
                    pygame.draw.line(self.screen, (0,0,0), ((x_dex*4+1)*self.screen_width/12, (y_dex*4+1)*self.screen_high/12), (((x_dex*4)+3)*self.screen_width/12,((y_dex*4)+3)*self.screen_high/12),5)
                    pygame.draw.line(self.screen, (0, 0, 0), ((x_dex*4+1)*self.screen_width / 12, ((y_dex*4)+3)*self.screen_high/12),(((x_dex*4)+3)* self.screen_width / 12, (y_dex*4+1)*self.screen_high/12),5)
                elif j == "O":
                    pygame.draw.circle(self.screen, (0,0,0), ((x_dex*2+1)*self.screen_width/6, (y_dex*2+1)*self.screen_high/6), self.screen_high/9, 5)
        pygame.display.flip()

    def add_to_board(self):
        self.click_y_index, self.click_x_index = self.indexing_pos()
        if self.board[self.click_y_index][self.click_x_index] == ".":
            self.board[self.click_y_index][self.click_x_index] = "O" if self.player %2 ==0 else "X"
            self.player += 1
        else:
            print("can't do that!")


    def click_on_screen(self, click_pos):
        self.click_x,self.click_y = click_pos
        return 0<self.click_x<self.screen_width and 0<self.click_y<self.screen_high

    def indexing_pos(self):
         return  int(self.click_y/self.screen_high*3), int(self.click_x/self.screen_width*3)

    def check_win(self):
        return (self.board[self.click_y_index][0]==self.board[self.click_y_index][1]==self.board[self.click_y_index][2]!=".") or (self.board[0][self.click_x_index]==self.board[1][self.click_x_index]==self.board[2][self.click_x_index]!='.') or (self.board[0][0]==self.board[1][1]==self.board[2][2]!='.') or (self.board[0][2]==self.board[1][1]==self.board[2][0]!=".")
    #############################
    def start_tic_tac_toe(self):
        self.running = True

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0] and self.click_on_screen(pygame.mouse.get_pos()):
                    print("in")
                    self.add_to_board()

                elif event.type == pygame.QUIT:
                    self.running = False

            self.display_board()
            if self.player>5 and self.check_win():
                print(f'player {self.player%2+1} won')
                time.sleep(10)
                self.running = False

        pygame.quit()

###############################################################################################
#_____________________________________________________________________________________________


if __name__ == "__main__":
    screen_size = (700, 700)  # (1280, 720)
    # pygame setup

    game = Tic_tac_toe(screen_size)

    game.start_tic_tac_toe()



