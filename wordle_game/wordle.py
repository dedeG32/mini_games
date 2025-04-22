"""
Guess the word game

TO-Do:
make modes: basic(word chosen based on difficulty), multiplayer (user1 type word, user2 need to guess it.), online (user guesses from a rondom word using an Api)
remake display
"""
import csv
import random
import time
from random import randint
from menu import get_int
from game import Game
import pygame

class Wordle(Game):
    def __init__(self):
        super().__init__()
        self.difficulty = self.ask_difficulty()

        self.word_to_find = self.set_word_to_find()
        self.set_life()
        self.guess_word= ["_"]*len(self.word_to_find)
        self.tries = 0
        self.used_letters= set()
        print(self.word_to_find, self.guess_word)
        self.font = self.set_font(30)

        self.debug = False

    def display_game(self):
        self.screen.fill("gray")
        self.display_board()
        self.display_word()

    def display_word(self):
        self.font = self.set_font(60)
        string = ""
        for i in self.guess_word:
            string = string +i + " "
        text = self.font.render(string, True, "black")
        self.screen.blit(text, (self.screen_width/2, self.screen_height/3))
        self.font = self.set_font(30)

    def display_board(self):
        for i in range(3):
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_height - i* self.screen_height/6 ),(self.screen_width, self.screen_height - i *self.screen_height  / 6), 5)
        for i in range(14):
            pygame.draw.line(self.screen,(0,0,0), (i* self.screen_width/13, 2*self.screen_height/3 ), (i* self.screen_width/13, self.screen_height), 5 )
        for i in range(0, 14):
            text = self.font.render(chr(ord('A')+i), True, self.color(i+ord('a')))
            self.screen.blit(text , (i * self.screen_width/13 +self.screen_width/26 , 9*self.screen_height/12))
        for i in range(0, 14):
            text = self.font.render(chr(ord('N')+i ), True, self.color(i+ord('n')))
            self.screen.blit(text , (i * self.screen_width/13 +self.screen_width/26 , 11*self.screen_height/12))

    def set_screen_resolution(self):
        self.screen_width = self.screen_resolution[0] * 0.8 if self.screen_resolution[0] < self.screen_resolution[1] else self.screen_resolution[1] * 0.8
        self.screen_height = self.screen_width * 0.7

    def color(self, i):
        if chr(i) in self.used_letters:
            if chr(i) in self.word_to_find:
                return "green"
            return "red"

        return "black"
    def ask_difficulty(self):

        print("select difficulty.")
        print("1. easy (4-9 letters word).")
        print("2. normal (8-13 letters word).")
        print("3. hard (13-19 letters word).")
        return get_int(1, 3)

    def set_life(self):
        print("Enter the number of life.(0 for infinite)")
        self.life = get_int(0,9999999999999)
        if self.life <= 0:
            self.life = None

    def set_word_to_find(self):
        difficulty = randint((4 if self.difficulty == 1 else 8 if self.difficulty ==2 else 13 ),(9 if self.difficulty == 1 else 13 if self.difficulty ==2 else 19 ))
        with open("words.csv", 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=":")
            for row in reader:
                if row[0] and int(row[0]) == difficulty:
                    return random.choice(list(eval(row[1])))

    def check_win(self) -> None:
        if self.life != None and self.life<=0:
            print("You lose!")
            self.screen.fill("gray")
            self.font = self.set_font(50)
            text = self.font.render("You lost", True, "Red")
            self.screen.blit(text , (self.screen_width/2,self.screen_height/2))
            pygame.display.flip()
            time.sleep(5)
            self.win = True

        elif self.found():
            print("You won!")
            self.screen.fill("gray")
            self.font = self.set_font(50)
            text = self.font.render("You won", True, "Green")
            self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
            pygame.display.flip()
            time.sleep(5)
            self.win = True

    def set_font(self, font_size = 12, font = 'test_sans.ttf'):
        return pygame.font.SysFont(None, font_size)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            print(event)
            print(event.unicode)
            if event.unicode in self.word_to_find:
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == event.unicode:
                        self.guess_word[i] = self.word_to_find[i]
            else:
                if self.life:
                    self.life-=1

            self.used_letters.add(event.unicode)


    def found(self):
        for i in range(len(self.word_to_find)):
            if self.word_to_find[i] != self.guess_word[i]:
                return False
        return True

    def debug_(self) -> None:
        print(self.life)
        # print(self.word_to_find)
        # print(self.guess_word)
        # print(self.life)
        # print(len(self.word_to_find))


if __name__ == "__main__":
    game = Wordle()
    game.start()