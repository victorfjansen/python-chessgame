from classes.piece.piece_model import PieceModel


class Piece(PieceModel):
    def __init__(self, color, king=False):
        PieceModel.__init__(self, color, king)
