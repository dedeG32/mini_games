from game import Game
import chess_board
import pygame


class Chess(Game):
    def __init__(self):
        self.screen_width, self.screen_height = (100,100)
        super().__init__()
        self.player = 0
        self.set_tick(1)
        self.chess_board = chess_board.Chessboard()
        self.chess_board.init_board()
        self.img_loading_chesspiecees()


    def display_game(self):
        self.screen.fill("white")
        self.display_board_line()
        self.display_chess_pieces()

    def display_board_line(self):
        for i in range(9):
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.screen_width / 8, 0),
                             (i* self.screen_width / 8, self.screen_height), 5)
        for i in range(9):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.screen_height / 8),
                             (self.screen_width ,i* self.screen_height / 8), 5)

    def display_chess_pieces(self):
        for i in range(8):
            for j in range(8):
                if not self.chess_board.board[i][j] == "XX":
                    self.screen.blit(self.pawn_img, (j *self.screen_width/8, i * self.screen_height/8))

    def img_loading_chesspiecees(self):
        self.rook_img = self.img_load_resize("test.png")
        self.queen_img = self.img_load_resize("test.png")
        self.king_img = self.img_load_resize("test.png")
        self.bishop_img = self.img_load_resize("test.png")
        self.knight_img = self.img_load_resize("test.png")
        self.pawn_img = self.img_load_resize("test.png")

    def img_load_resize(self, image):
        return self.img_resize(self.img_load(image), self.screen_width/9, self.screen_height/9)


    def set_screen_resolution(self):
        self.screen_width = self.screen_resolution[0] * 0.85 if self.screen_resolution[0]<self.screen_resolution[1] else self.screen_resolution[1] *0.85
        self.screen_height = self.screen_width


if __name__ == "__main__":
    game = Chess()
    game.start()

