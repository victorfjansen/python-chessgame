from abc import ABC, abstractmethod
from classes.piece.piece import Piece


class EnemyContract(ABC):
    @abstractmethod
    def move_piece(self, game):
        pass

    @abstractmethod
    def get_random_piece_with_legal_moves(board, game) -> (Piece, (int, int), (int, int)):
        pass
