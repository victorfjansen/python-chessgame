from classes.board.board import Board
from classes.enemy.enemy_contract import EnemyContract
from classes.graphics.graphics import Graphics
from classes.menu.menu import MainMenu
from constants.colors import COLORS
from constants.difficulty import DifficultyLevel


class GameModel:
    def __init__(self):
        self.__graphics = Graphics()
        self.__board = Board()

        self.__main_menu = MainMenu()

        #primeiro turno
        self.__turn = COLORS.BLUE.value

        # localização do board
        self.__selected_piece = None

        #verifica se uma peça foi capturada
        self.__hop = False
        self.__selected_legal_moves = []

        self.__mouse_pos = None

        self.__difficulty_level = DifficultyLevel.EASY.value
        self.__enemy_turn = COLORS.RED.value

        self.__enemy = None
        self.__end_game = False

    def get_graphics(self):
        return self.__graphics

    def set_graphics(self, graphics):
        self.__graphics = graphics

    def get_board(self):
        return self.__board

    def set_board(self, board):
        self.__board = board

    def get_turn(self):
        return self.__turn

    def set_turn(self, turn):
        self.__turn = turn

    def get_selected_piece(self):
        return self.__selected_piece

    def set_selected_piece(self, piece):
        self.__selected_piece = piece

    def get_hop(self):
        return self.__hop

    def set_hop(self, hop):
        self.__hop = hop

    def get_selected_legal_moves(self):
        return self.__selected_legal_moves

    def set_selected_legal_moves(self, legal_moves):
        self.__selected_legal_moves = legal_moves

    def get_mouse_pos(self):
        return self.__mouse_pos

    def set_mouse_pos(self, mouse_pos):
        self.__mouse_pos = mouse_pos

    def set_main_menu(self, main_menu):
        self.__main_menu = main_menu

    def get_main_menu(self):
        return self.__main_menu
    
    def set_difficulty_level(self, value, level):
        self.__difficulty_level = level

    def get_difficulty_level(self):
        return self.__difficulty_level

    def set_enemy_turn(self, enemy_turn):
        self.__enemy_turn = enemy_turn

    def get_enemy_turn(self):
        return self.__enemy_turn

    def set_enemy(self, enemy):
        self.__enemy = enemy

    def get_enemy(self) -> EnemyContract:
        return self.__enemy

    def set_end_game(self, value):
        self.__end_game = value

    def get_end_game(self):
        return self.__end_game



