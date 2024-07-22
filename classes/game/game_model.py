from classes.board.board import Board
from classes.graphics.graphics import Graphics
from constants.colors import COLORS


class GameModel:
    def __init__(self):
        self.__graphics = Graphics()
        self.__board = Board()

        #primeiro turno
        self.__turn = COLORS.BLUE.value

        # localização do board
        self.__selected_piece = None

        #verifica se uma peça foi capturada
        self.__hop = False
        self.__selected_legal_moves = []

        self.__mouse_pos = None

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
