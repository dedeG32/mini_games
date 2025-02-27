from game import Game
import pygame
import random
class Pong(Game):
    class Player:
        def __init__(self, pong, pos, up_key ,down_key, color):
            self.pong = pong
            self.score = 0
            self.pos_x, self.pos_y = pos
            self.tall = self.pong.screen_height * 0.15  #player tall acoordinc to the screen resolution
            self.up_key ,self.down_key = up_key, down_key
            self.velocity = 0.2
            self.can_move = False, False
            self.color = color
            #self.rect = pygame.Rect((self.pos_x, self.pos_y, self.pos_x, self.pos_y))
            self.rect = self.init_rect()

        def move(self):#, up_down_variable):
            #print(self.can_move)
            if self.can_move[0]:
                match self.can_move[1]:
                    case -1:
                        if self.pos_y > 0:
                            self.pos_y += self.can_move[1] * self.velocity
                    case 1:
                        if self.pos_y < self.pong.screen_height -self.tall:
                            self.pos_y += self.can_move[1] * self.velocity  # up_down_variable



        def init_rect(self):
            return pygame.Rect((self.pos_x, self.pos_y, self.pong.screen_width * 0.01, self.tall))

        def draw(self):
            pygame.draw.rect(self.pong.screen, self.color, self.init_rect())

        def events(self, keys, bool_val):
            if keys[self.up_key]:
                self.can_move = bool_val, -1

            elif keys[self.down_key]:
                self.can_move = bool_val, 1



            '''if event.key == self.up_key:
                    self.move(1)
                    print(f"move {self.up_key} done")
            elif event.key == self.down_key:
                    self.move(-1)'''

        # def __call__(self):
        #     return self.player_rec


    class Ball:
        def __init__(self, pong, pos):
            self.pong = pong
            self.pos_x, self.pos_y = pos
            self.velocity_x, self.velocity_y = 1,1
            self.direction_x, self.direction_y = 1,1 #random.Random.choice((-1, 1)), random.Random.choice((-1,1))
            self.rect = self.init_rect()

        def move(self):
            self.pos_x += self.velocity_x * self.direction_x
            self.pos_y += self.velocity_y * self.direction_y


        def bounce(self):
            if self.pos_y <= 0 or self.pos_y >= self.pong.screen_height:
                self.direction_y *= -1

            elif self.pos_x == self.pong.player2 or self.pos_x == self.pong.player1:
                pass
            #To change ####################### bouncing oon wall instead of player
            elif self.pos_x < 0 or self.pos_x >= self.pong.screen_width:
                self.direction_x *= -1
                self.velocity_x *= 1.02
                #print("suposed win")


        def init_rect(self):
            return self.pos_x, self.pos_y, self.pong.screen_height*0.02, self.pong.screen_height*0.02

        def draw(self):
            pygame.draw.rect(self.pong.screen, (0,0,0), self.init_rect())

        def events(self):
            pass

    def __init__(self):
        super().__init__()
        self.player1 = self.Player(self, (self.screen_width* 0.95, self.screen_height/2), pygame.K_UP, pygame.K_DOWN, (255,0,0))
        self.player2 = self.Player(self, (self.screen_width* 0.05, self.screen_height/2), pygame.K_w, pygame.K_s, (0,255,0))
        self.ball = self.Ball(self, (self.screen_width/2, self.screen_height/2))

    def check_collision(self):
        pass

    def set_screen_resolution(self):
        self.screen_width , self.screen_height=  self.screen_resolution[0]*0.9, self.screen_resolution[1]*0.9

    def display_game(self):
        self.screen.fill("white")
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()

    def check_win(self):
        pass

    def action(self) -> None:
        self.ball.bounce()
        self.ball.move()
        self.player1.move()
        self.player2.move()


    def events(self, event) -> None:
        self.ball.events()
        if event.type == pygame.KEYDOWN:
            print("key pressed")
            keys = pygame.key.get_pressed()
            self.player1.events(keys, True)
            self.player2.events(keys, True)
        elif event.type == pygame.KEYUP:
            print("key released")
            keys = pygame.key.get_pressed()
            self.player1.events(keys, False)
            self.player2.events(keys, False)





if __name__ == '__main__':
    pong = Pong()
    pong.start()