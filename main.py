import pygame
from pygame.locals import *

from classes.game import Game

if __name__ == "__main__":
    pygame.font.init()
    game = Game()
    game.main()