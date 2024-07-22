class SquareModel:
    def __init__(self, color, occupant=None):
        self.__color = color
        self.__occupant = occupant

    def set_color(self, color):
        self.__color = color

    def set_occupant(self, occupant):
        self.__occupant = occupant

    def get_color(self):
        return self.__color

    def get_occupant(self):
        return self.__occupant
