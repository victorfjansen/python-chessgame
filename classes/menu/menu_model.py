
import pygame


class MenuModel:
    def __init__(self):
        self.__surface = pygame.display.set_mode((600, 600))

    def get_surface(self):
        return self.__surface
    
    def set_surface(self, value):
        self.__surface = value
