# import pygame, sys
# from pygame.locals import *
#
# BLACK = ( 0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = ( 255, 0, 0)
#
# pygame.init()
# size = (700, 500)
# screen = pygame.display.set_mode(size)
#
# DISPLAYSURF = pygame.display.set_mode(size)
# pygame.display.set_caption('P.Earth')
#
#
# font = pygame.font.Font(None, 25)
#
# while 1: # main game loop
#
#     text = font.render("You win!", True, WHITE)
#     text_rect = text.get_rect(center=(size[0] / 2, size[1] / 2))
#     screen.blit(text, text_rect)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.display.update()
#     pygame.display.flip()


# string = "hello 1world"
# # if {1,2,3,4,5,6,7,8,9} in string:
# #     print("true")
#
# for i in string:
#     print(i in "123456789")


"testing csv rows"
# import random
# import csv
# word_to_find = ""
# difficulty = random.randint(4,19)
# print(difficulty)
# with open("words.csv", 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile, delimiter=":")
#     for row in reader:
#         print(row[0])
#         print(list(eval(row[1])))
#
#         if row[0] and int(row[0]) == difficulty:
#
#             word_to_find = random.choice(list(eval(row[1])))
#
# print( word_to_find)

"testing list setting"
print(["_"]*10)