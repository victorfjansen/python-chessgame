import pygame
import pygame_menu

from classes.menu.menu_contract import MenuContract
from classes.menu.menu_model import MenuModel
from constants.difficulty import DifficultyLevel


class MainMenu(MenuModel, MenuContract):
    def __init__(self):
        pygame.init()
        MenuModel.__init__(self)

    def setup_menu(self, game):
        menu = pygame_menu.Menu('Selecione seu modo de jogo! ', 600, 600,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Jogar!', game.init_game_main_loop)
        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.add.selector('Nível :', [('Fácil', DifficultyLevel.EASY.value), ('Médio', DifficultyLevel.MEDIUM.value), ('Difícil', DifficultyLevel.HARD.value)],
                          onchange=game.set_difficulty_level)
        menu.mainloop(self.get_surface())
