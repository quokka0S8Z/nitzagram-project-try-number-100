import pygame
from constants import *
from helpers import screen
class Comment:
    def __init__(self, text):
        self.text = text
    def display(self, index):
        comment_font = pygame.font.SysFont("chalkduster.ttf", COMMENT_TEXT_SIZE)
        comment_to_display = comment_font.render(self.text, True, BLACK)
        comment_y_pos = FIRST_COMMENT_Y_POS + (index * COMMENT_LINE_HEIGHT)
        screen.blit(comment_to_display, (FIRST_COMMENT_X_POS, comment_y_pos))


