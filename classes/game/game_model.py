from classes.board.board import Board
from classes.graphics.graphics import Graphics
from constants.colors import COLORS


class GameModel:
    def __init__(self):
        self._graphics = Graphics()
        self._board = Board()

        #primeiro turno
        self._turn = COLORS.BLUE.value

        # localização do board
        self._selected_piece = None

        #verifica se uma peça foi capturada
        self._hop = False
        self._selected_legal_moves = []

        self._mouse_pos = None

    def get_graphics(self):
        return self._graphics

    def set_graphics(self, graphics):
        self._graphics = graphics

    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def get_turn(self):
        return self._turn

    def set_turn(self, turn):
        self._turn = turn

    def get_selected_piece(self):
        return self._selected_piece

    def set_selected_piece(self, piece):
        self._selected_piece = piece

    def get_hop(self):
        return self._hop

    def set_hop(self, hop):
        self._hop = hop

    def get_selected_legal_moves(self):
        return self._selected_legal_moves

    def set_selected_legal_moves(self, legal_moves):
        self._selected_legal_moves = legal_moves

    def get_mouse_pos(self):
        return self._mouse_pos

    def set_mouse_pos(self, mouse_pos):
        self._mouse_pos = mouse_pos
