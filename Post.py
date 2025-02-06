import pygame
from Comment import *
from constants import *
from helpers import screen


class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = comments

    def add_like(self):
        self.likes_counter += 1
    def add_comment(self, text):
        if isinstance(text, Comment):
            self.comments.append(text)
    def display(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        description_surface = font.render(self.description, True, BLACK)
        screen.blit(description_surface, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        location_surface = font.render(self.location, True, GREY)
        screen.blit(location_surface, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        likes_surface = font.render(f"{self.likes_counter} likes", True, BLACK)
        screen.blit(likes_surface, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



