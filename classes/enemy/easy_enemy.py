from classes.enemy.enemy_contract import EnemyContract
from classes.piece.piece import Piece
import random


class EasyEnemy(EnemyContract):
    def __init__(self):
        print("EASY ENEMY SELECTED")

    def get_random_piece_with_legal_moves(self, board, game) -> (Piece, (int, int), (int, int)):
        pieces_with_moves = []

        for x in range(8):
            for y in range(8):
                piece = board.get_matrix()[x][y].get_occupant()
                if piece is not None and piece.get_color() == game.get_enemy_turn():
                    legal_moves = board.legal_moves((x, y))
                    if legal_moves:
                        pieces_with_moves.append(((x, y), legal_moves[0], piece))

        if pieces_with_moves:
            random_piece = random.choice(pieces_with_moves)
            return random_piece[2], random_piece[1], random_piece[0]  # Retorna a peça com movimentos legais
        else:
            return None  # Nenhuma peça tem movimentos legais

    def move_piece(self, game):
        selected_piece, coord_to_go, coords = self.get_random_piece_with_legal_moves(game.get_board(), game)

        game.set_selected_piece(coords)
        game.get_board().move_piece(coords, coord_to_go)

        if coord_to_go not in game.get_board().adjacent(coords):
            # faz uma media e pega a peça do meio, a partir da referência e da nova peça
            game.get_board().remove_piece((
                (game.get_selected_piece()[0] + coord_to_go[0]) // 2,
                (game.get_selected_piece()[1] + coord_to_go[1]) // 2))

            # seta a captura como true
            game.set_hop(True)
            game.set_selected_piece(coord_to_go)

        if game.get_hop():
            # se houver uma peça capturada e ainda houver movimentos "legais"

            legal_moves = game.get_board().legal_moves(game.get_selected_piece(), game.get_hop())

            if (game.get_selected_piece() is not None and game.get_selected_piece() in
                    legal_moves):
                # faz a movimentação da peça
                game.get_board().move_piece(game.get_selected_piece(), legal_moves[0])
                game.get_board().remove_piece(
                    ((game.get_selected_piece()[0] + legal_moves[0][0]) // 2,
                     (game.get_selected_piece()[1] + legal_moves[0][1]) // 2))

                game.end_turn()
            game.end_turn()
        else:
            game.end_turn()
