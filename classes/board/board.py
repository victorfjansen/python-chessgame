from typing import Any, List

from classes.board.board_contract import BoardContract
from classes.board.board_model import BoardModel
from classes.piece.piece import Piece
from classes.square.square import Square
from constants.colors import COLORS
from constants.directions import Directions


class Board(BoardModel, BoardContract):
    def __init__(self):
        BoardModel.__init__(self)
        self.set_matrix(self.new_board())

    def new_board(self) -> List[List[None or int]]:
        # Inicializa os quadrados e coloca-os em matriz
        matrix: List[List[None or int]] = [[None] * 8 for i in range(8)]
        for x in range(8):
            for y in range(8):
                if (x % 2 != 0) and (y % 2 == 0):
                    matrix[y][x] = Square(COLORS.WHITE.value)
                elif (x % 2 != 0) and (y % 2 != 0):
                    matrix[y][x] = Square(COLORS.BLACK.value)
                elif (x % 2 == 0) and (y % 2 != 0):
                    matrix[y][x] = Square(COLORS.WHITE.value)
                elif (x % 2 == 0) and (y % 2 == 0):
                    matrix[y][x] = Square(COLORS.BLACK.value)

        # Inicializa as peças nas casas
        for x in range(8):
            for y in range(3):
                if matrix[x][y].get_color() == COLORS.BLACK.value:
                    matrix[x][y].set_occupant(Piece(COLORS.RED.value))
            for y in range(5, 8):
                if matrix[x][y].get_color() == COLORS.BLACK.value:
                    matrix[x][y].set_occupant(Piece(COLORS.BLUE.value))

        return matrix

    def board_string(self, board):
        # Pega o board em string e localiza os quadrados pretos e brancos
        board_string = [[None] * 8] * 8

        for x in range(8):
            for y in range(8):
                if board[x][y].get_color() == COLORS.WHITE.value:
                    board_string[x][y] = "WHITE"
                else:
                    board_string[x][y] = "BLACK"

        return board_string

    def position(self, direction, pixel):
        # Devolve as posições a partir da direção dada.
        x = pixel[0]
        y = pixel[1]
        if direction == Directions.NORTHEAST.value:
            return x - 1, y - 1
        elif direction == Directions.NORTHWEST.value:
            return x + 1, y - 1
        elif direction == Directions.SOUTHWEST.value:
            return x - 1, y + 1
        elif direction == Directions.SOUTHEAST.value:
            return x + 1, y + 1
        else:
            return 0

    def adjacent(self, pixel):
        # retorna uma lista de posições adjacentes à posição fornecida
        x = pixel[0]
        y = pixel[1]

        return [self.position(Directions.NORTHEAST.value, (x, y)), self.position(Directions.NORTHWEST, (x, y)),
                self.position(Directions.SOUTHWEST.value, (x, y)),
                self.position(Directions.SOUTHEAST.value, (x, y))]

    def location(self, pixel) -> Any:
        x = pixel[0]
        y = pixel[1]

        return self.get_matrix()[x][y]

    def blind_legal_moves(self, pixel):
        # Retorna uma lista de movimentos que podem ser feitos, mas ainda não foram jogados
        x = pixel[0]
        y = pixel[1]
        if self.get_matrix()[x][y].get_occupant() is not None:

            if (not self.get_matrix()[x][y].get_occupant().get_king() and
                    self.get_matrix()[x][y].get_occupant().get_color() == COLORS.BLUE.value):
                blind_legal_moves = [self.position(Directions.NORTHWEST.value, (x, y)),
                                     self.position(Directions.NORTHEAST.value, (x, y))]

            elif (not self.get_matrix()[x][y].get_occupant().get_king() and
                  self.get_matrix()[x][y].get_occupant().get_color() == COLORS.RED.value):
                blind_legal_moves = [self.position(Directions.SOUTHWEST.value, (x, y)),
                                     self.position(Directions.SOUTHEAST.value, (x, y))]

            else:
                blind_legal_moves = [self.position(Directions.NORTHEAST.value, (x, y)),
                                     self.position(Directions.NORTHWEST.value, (x, y)),
                                     self.position(Directions.SOUTHWEST.value, (x, y)),
                                     self.position(Directions.SOUTHEAST.value, (x, y))]

        else:
            blind_legal_moves = []

        return blind_legal_moves

    def legal_moves(self, pixel, hop=False):
        # retorna uma lista de posições que podem ser jogadas a partir das posições que não foram jogadas

        x = pixel[0]
        y = pixel[1]
        blind_legal_moves = self.blind_legal_moves((x, y))
        legal_moves = []

        if not hop:  # se já jouve uma peça capturada. No caso, se não.
            for move in blind_legal_moves:
                if not hop:
                    if self.on_board(move):
                        if self.location(move).get_occupant() is None:
                            legal_moves.append(move)

                        # verifica as posições possíveis para movimentação
                        # se está no board, se há outra peça no local, se há outra peça da mesma cor
                        elif self.location(move).get_occupant().get_color() != self.location(
                                (x, y)).get_occupant().get_color() and self.on_board(
                            (move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (
                                move[0] - x), move[1] + (
                                move[1] - y))).get_occupant() is None:
                            legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

        else:  # se já jouve uma peça capturada. No caso, se sim.
            for move in blind_legal_moves:
                if self.on_board(move) and self.location(move).get_occupant() is not None:
                    if self.location(move).get_occupant().get_color() is not self.location((x, y)).get_occupant().get_color() and self.on_board(
                            (move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (
                            move[0] - x), move[1] + (
                            move[1] - y))).get_occupant() is None:
                        legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

        return legal_moves

    def remove_piece(self, pixel):
        # Remove a peça do board
        x = pixel[0]
        y = pixel[1]
        self.get_matrix()[x][y].set_occupant(None)

    def move_piece(self, pixel_start, pixel_end):
        # move a peça de uma posição a outra (tuplas)
        start_x = pixel_start[0]
        start_y = pixel_start[1]
        end_x = pixel_end[0]
        end_y = pixel_end[1]

        self.get_matrix()[end_x][end_y].set_occupant(self.get_matrix()[start_x][start_y].get_occupant())
        self.remove_piece((start_x, start_y))

        self.verify_and_set_king((end_x, end_y))

    def is_end_square(self, coords):
        # verifica se está no quadrado final (bordas)
        if coords[1] == 0 or coords[1] == 7:
            return True
        else:
            return False

    def on_board(self, pixel):
        # verifica se de fato o quadrado está no board. Se não está "fora".
        x = pixel[0]
        y = pixel[1]
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False
        else:
            return True

    def verify_and_set_king(self, pixel):
        # verifica se a peça está na posição do rei. Se estiver, seta o King como True.
        x = pixel[0]
        y = pixel[1]
        if self.location((x, y)).get_occupant() is not None:
            if (self.location((x, y)).get_occupant().get_color() == COLORS.BLUE.value and y == 0) or (
                    self.location((x, y)).get_occupant().get_color() == COLORS.RED.value and y == 7):
                self.location((x, y)).get_occupant().set_king(True)
