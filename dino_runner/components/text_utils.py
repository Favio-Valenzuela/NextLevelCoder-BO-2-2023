import pygame
from dino_runner.utils.constants import FONT_STYLE, COLORS, SCREEN_HEIGHT, SCREEN_WIDTH

class TextUtils:
    
    def get_score_element(self, points):
        font = pygame.font.Font(FONT_STYLE[1],22)
        text = font.render("Points: "+ str(points), True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        return text, text_rect
    
    def get_centered_message(self, message, width =SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2 ):
        font = pygame.font.Font(FONT_STYLE[1], 30)
        text = font.render(message, True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text, text_rect
    
    def get_shield_time(self, time_to_show):
        font = pygame.font.Font(FONT_STYLE[1], 20)
        text = font.render(str(time_to_show), True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (1000,380)
        return text, text_rect