import pygame
import pygame_menu

from classes.menu.menu_contract import MenuContract
from classes.menu.menu_model import MenuModel
from constants.difficulty import DifficultyLevel


class MainMenu(MenuModel, MenuContract):
    def __init__(self):
        pygame.init()
        MenuModel.__init__(self)

    def has_data_on_store(self, game) -> bool:
        return game.get_board_store().has_stored_data()

    def setup_menu(self, game):
        menu = pygame_menu.Menu('Selecione seu modo de jogo! ', 600, 600,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Jogar!', game.init_game_main_loop)

        if game.get_board_store().has_stored_data():
            menu.add.button('Retomar partida anterior!', game.load_stored_game)

        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.add.selector('Nível :', [('Fácil', DifficultyLevel.EASY.value), ('Médio', DifficultyLevel.MEDIUM.value),  ('LOCAL', DifficultyLevel.LOCAL.value)],
                          onchange=game.set_difficulty_level)
        menu.mainloop(self.get_surface())
