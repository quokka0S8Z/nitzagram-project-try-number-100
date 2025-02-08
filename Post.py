import pygame
from Comment import *
from constants import *
from helpers import screen


class Post:
    def __init__(self, username, location, description, ):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0
    def add_like(self):
        self.likes_counter += 1
    def add_comment(self, text):
        if isinstance(text, Comment):
            self.comments.append(text)
    def display(self):
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()
    def display_content(self):
        pass
    def display_header(self):
        location_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        location_to_display = location_font.render(self.location, True, (134,134,134))
        screen.blit(location_to_display, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        description_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
        description_to_display = description_font.render(self.location, True, (50, 50, 50))
        screen.blit(description_to_display, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        user_name_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
        user_name_to_display = user_name_font.render(self.username, True, (50, 50, 50))
        screen.blit(user_name_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))
    def display_likes(self):
        like_text = "Liked by" + str(self.likes_counter) + "users"
        like_text_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        like_to_display = like_text_font.render(like_text, True, (0,0,0))
        screen.blit(like_to_display, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
    def display_comments(self):
        position_index = self.comments_display_index
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



