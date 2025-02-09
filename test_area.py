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
