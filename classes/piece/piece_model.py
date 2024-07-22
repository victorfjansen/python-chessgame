class PieceModel:
    def __init__(self, color, king=False):
        self._color = color
        self._king = king

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_king(self, king):
        self._king = king

    def get_king(self):
        return self._king
