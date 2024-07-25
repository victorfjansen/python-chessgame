from abc import ABC, abstractmethod
from typing import List, Any


class BoardContract(ABC):
    @abstractmethod
    def new_board(self) -> List[List[None or int]]:
        pass
    
    @abstractmethod
    def position(self, direction, pixel):
        pass

    @abstractmethod
    def adjacent(self, pixel):
        pass

    @abstractmethod
    def location(self, pixel) -> Any:
        pass

    @abstractmethod
    def blind_legal_moves(self, pixel):
        pass

    @abstractmethod
    def legal_moves(self, pixel, hop=False):
        pass

    @abstractmethod
    def remove_piece(self, pixel):
        pass

    @abstractmethod
    def move_piece(self, pixel_start, pixel_end):
        pass

    @abstractmethod
    def is_end_square(self, coords):
        pass

    @abstractmethod
    def on_board(self, pixel):
        pass

    @abstractmethod
    def verify_and_set_king(self, pixel):
        pass