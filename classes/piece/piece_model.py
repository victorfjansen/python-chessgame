class PieceModel:
    def __init__(self, color, king=False):
        self.__color = color
        self.__king = king

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_king(self, king):
        self.__king = king

    def get_king(self):
        return self.__king
