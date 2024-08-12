from abc import ABC, abstractmethod


class GraphicsContract(ABC):
    @abstractmethod
    def setup_window(self):
        pass

    @abstractmethod
    def update_display(self, board, legal_moves, selected_piece):
        pass

    @abstractmethod
    def draw_board_pieces(self, board):
        pass

    @abstractmethod
    def pixel_coords(self, board_coords):
        pass

    @abstractmethod
    def board_coords(self, pixel):
        pass

    @abstractmethod
    def highlight_squares(self, squares, origin):
        pass

    @abstractmethod
    def draw_message(self, message):
        pass
