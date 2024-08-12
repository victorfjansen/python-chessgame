from time import sleep
from classes.enemy.enemy_contract import EnemyContract
from classes.piece.piece import Piece
from constants.directions import Directions
import random

class MediumEnemy(EnemyContract):
    def __init__(self):
        print("MEDIUM ENEMY SELECTED")

    def get_random_piece_with_adjacent(self, board, game) -> (Piece, (int, int), (int, int)):
        pieces_with_adjacent = []
        pieces_without_adjacent = []

        for x in reversed(range(8)):
            for y in reversed(range(8)):
                piece = board.get_matrix()[x][y].get_occupant()
                if piece is not None and piece.get_color() == game.get_enemy_turn():
                    legal_moves = board.legal_moves((x, y))
                    if legal_moves:
                        adjacent_squares = board.adjacent((x, y))
                        has_adjacent_piece = [
                            square for square in adjacent_squares
                            if isinstance(square, tuple) and board.on_board(square) and
                               board.location(square).get_occupant() is not None and
                               board.location(square).get_occupant().get_color() != game.get_enemy_turn()
                        ]

                        if len(has_adjacent_piece) > 0:
                            is_king_piece = (board.location((x, y)).get_occupant() and board.location((x, y))
                                             .get_occupant().get_king())

                            if not is_king_piece:
                                west_position = board.on_board(
                                    board.position(Directions.SOUTHWEST.value, (x, y))) and board.location(
                                    board.position(Directions.SOUTHWEST.value, (x, y))).get_occupant()
                                southwest = west_position and west_position.get_color() != game.get_enemy_turn()

                                if southwest:
                                    pieces_with_adjacent.append(((x, y), legal_moves[0], piece))
                                else:
                                    position = legal_moves[1] if len(legal_moves) > 1 else legal_moves[0]
                                    pieces_with_adjacent.append(((x, y), position, piece))

                            else:
                                south_west_position = board.on_board(
                                    board.position(Directions.SOUTHWEST.value, (x, y))) and board.location(
                                    board.position(Directions.SOUTHWEST.value, (x, y))).get_occupant()

                                south_heast_position = board.on_board(
                                    board.position(Directions.SOUTHEAST.value, (x, y))) and board.location(
                                    board.position(Directions.SOUTHEAST.value, (x, y))).get_occupant()

                                north_heast_position = board.on_board(
                                    board.position(Directions.NORTHEAST.value, (x, y))) and board.location(
                                    board.position(Directions.NORTHEAST.value, (x, y))).get_occupant()

                                north_west_position = board.on_board(
                                    board.position(Directions.NORTHWEST.value, (x, y))) and board.location(
                                    board.position(Directions.NORTHWEST.value, (x, y))).get_occupant()

                                southwest = south_west_position and south_west_position.get_color() != game.get_enemy_turn() and board.on_board(board.position(Directions.SOUTHWEST.value, board.position(Directions.SOUTHWEST.value, (x, y)))) and not board.location(board.position(Directions.SOUTHWEST.value, board.position(Directions.SOUTHWEST.value, (x, y)))).get_occupant()
                                southeast = south_heast_position and south_heast_position.get_color() != game.get_enemy_turn() and board.on_board(board.position(Directions.SOUTHEAST.value, board.position(Directions.SOUTHEAST.value, (x, y)))) and not board.location(board.position(Directions.SOUTHEAST.value, board.position(Directions.SOUTHEAST.value, (x, y)))).get_occupant()
                                northeast = north_heast_position and north_heast_position.get_color() != game.get_enemy_turn() and board.on_board(board.position(Directions.NORTHEAST.value, board.position(Directions.NORTHEAST.value, (x, y)))) and not board.location(board.position(Directions.NORTHEAST.value, board.position(Directions.NORTHEAST.value, (x, y)))).get_occupant()
                                northwest = north_west_position and north_west_position.get_color() != game.get_enemy_turn() and board.on_board(board.position(Directions.NORTHWEST.value, board.position(Directions.NORTHWEST.value, (x, y)))) and not board.location(board.position(Directions.NORTHWEST.value, board.position(Directions.NORTHWEST.value, (x, y)))).get_occupant()

                                if southwest:
                                    pieces_with_adjacent.append(((x, y), board.position(Directions.SOUTHWEST.value, board.position(Directions.SOUTHWEST.value, (x, y))), piece))
                                if southeast:
                                    pieces_with_adjacent.append(((x, y), board.position(Directions.SOUTHEAST.value, board.position(Directions.SOUTHEAST.value, (x, y))), piece))
                                if northwest:
                                    pieces_with_adjacent.append(((x, y), board.position(Directions.NORTHWEST.value, board.position(Directions.NORTHWEST.value, (x, y))), piece))
                                if northeast:
                                    pieces_with_adjacent.append(((x, y), board.position(Directions.NORTHEAST.value, board.position(Directions.NORTHEAST.value, (x, y))), piece))

                        else:
                            pieces_without_adjacent.append(((x, y), legal_moves[0], piece))

        if pieces_with_adjacent:
            random_piece = random.choice(pieces_with_adjacent)
            return random_piece[2], random_piece[1], random_piece[0]
        elif pieces_without_adjacent:
            random_piece = random.choice(pieces_without_adjacent)
            return random_piece[2], random_piece[1], random_piece[0]
        else:
            return self.get_random_piece_with_adjacent(board, game)


    def move_piece(self, game):
        selected_piece, coord_to_go, coords = self.get_random_piece_with_adjacent(game.get_board(), game)

        game.set_selected_piece(coords)
        game.set_selected_legal_moves([coord_to_go])

        game.update()
        sleep(0.3)
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

            if (game.get_selected_piece() is not None and game.get_board().adjacent(game.get_selected_piece()) in
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
