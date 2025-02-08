import pygame
from Post import Post
from constants import *
from helpers import screen
class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        screen.fill(self.background_color)
        super().display()

    def display_content(self):
        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        text_surface = font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (0.15 * WINDOW_WIDTH, 0.4 * WINDOW_HEIGHT))