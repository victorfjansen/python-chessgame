from classes.square.square_model import SquareModel


class Square(SquareModel):
    def __init__(self, color, occupant=None):
        SquareModel.__init__(self, color, occupant)
