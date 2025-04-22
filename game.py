import pygame
import pygame.freetype

pygame.init()
class Game(object):

    screen_resolution = pygame.display.Info().current_w, pygame.display.Info().current_h
    """
    A model class, parent of every game class
    """
    def __init__(self):  # , surface):
        self.set_screen_resolution()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.win = False
        self.debug = False


    def set_screen_resolution(self, resolution: (int,int) = None):
        if resolution:
            self.screen_resolution, self.screen_height = resolution
        else:
            self.screen_width, self.screen_height = self.screen_resolution
    def click_on_screen(self) -> bool:
        """
        Checks if the click have been done on the pygame window. And refresh the self.x and self.y variable of the mouse
        :param click_pos:
        :return:
        """
        self.click_x,self.click_y = pygame.mouse.get_pos()
        return 0<self.click_x<self.screen_width and 0<self.click_y<self.screen_height

    def set_font(self, font_size = 12, font = 'test_sans.ttf'):
        #return pygame.freetype.Font(font, font_size)
        return pygame.font.SysFont(None, font_size)
    def set_tick(self, tick = 10):
        clock = pygame.time.Clock()
        clock.tick(tick)  # limits FPS to 10

    def events(self, event):#, event) -> None:
        """
        handles all the user input. Note that the exit event is doesn't need to be handled.
        :return:
        """
        pass

    def display_game(self) -> None:
        """
        draw the game content on a pygame window
        :return:
        """
        pass

    def check_win(self) -> None:
        """
        proceed to the end game steps if win
        :return:
        """
        pass

    def action(self) -> None:
        """
        contain main mechanic of the game, actions that need to be repeted for each frame, regardless of events
        :return:
        """
        pass

    def debug_(self) -> None:
        """
        Have the print statement that are needed to unsure the game is running properly. It is repeated for each interation
        """
        pass

    def img_load(self, image):
        return pygame.image.load(image)

    def img_resize(self, image, width,height):
        return pygame.transform.scale(image, (width,height) )

    def start(self):

        while not self.win:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.win = True
                else:
                    self.events(event)  # event)

            self.display_game()
            pygame.display.flip()
            self.action()
            if self.debug:
                self.debug_()
            self.check_win()

        pygame.quit()


    def __repr__(self):
        return f"{type(self).__name__}(screen_width={self.screen_width}"



if __name__ == "__main__":
    game = Game()
    game.start()