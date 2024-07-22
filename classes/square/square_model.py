class SquareModel:
    def __init__(self, color, occupant=None):
        self._color = color
        self._occupant = occupant

    def set_color(self, color):
        self._color = color

    def set_occupant(self, occupant):
        self._occupant = occupant

    def get_color(self):
        return self._color

    def get_occupant(self):
        return self._occupant
