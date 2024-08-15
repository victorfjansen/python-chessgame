from time import sleep
from classes.enemy.enemy_contract import EnemyContract
from classes.piece.piece import Piece
from constants.directions import Directions
import random

from constants.colors import COLORS

class MediumEnemy(EnemyContract):
    def __init__(self):
        print("CHANGED MEDIUM ENEMY SELECTED")

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

    def get_better_movement_without_adjacent(self, board, pieces_without_adjacent):
        better_movement = []
        for movement in pieces_without_adjacent:
            current_position = movement[0]
            coord_to_go = movement[1]

            direction = board.get_direction_from_coords(current_position, coord_to_go)

            next_direction_position = board.on_board(
                board.position(direction, coord_to_go)) and board.location(
                board.position(direction, coord_to_go)).get_occupant()

            direction_correspondent = None

            if direction == Directions.SOUTHWEST.value:
                direction_correspondent = board.on_board(
                    board.position(Directions.SOUTHEAST.value, coord_to_go)) and board.location(
                    board.position(Directions.SOUTHEAST.value, coord_to_go)).get_occupant()

            if direction == Directions.SOUTHEAST.value:
                direction_correspondent = board.on_board(
                    board.position(Directions.SOUTHWEST.value, coord_to_go)) and board.location(
                    board.position(Directions.SOUTHWEST.value, coord_to_go)).get_occupant()

            if not next_direction_position and not direction_correspondent:
                better_movement.append(movement)

            if len(better_movement) == 0 and movement == pieces_without_adjacent[-1]:
                better_movement.append(movement)
        return better_movement


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
            random_piece = (self.get_better_movement_without_adjacent(board, pieces_without_adjacent))[-1]
            return random_piece[2], random_piece[1], random_piece[0]
        else:
            return None

    def should_get_next_hop(self, game, board, selected_piece_coord):
        next_hop_movements = []
        is_king_piece = board.location(selected_piece_coord).get_occupant().get_king() if board.location(selected_piece_coord).get_occupant() else False

        if not is_king_piece:
            south_west_position = board.on_board(
                board.position(Directions.SOUTHWEST.value, selected_piece_coord)) and board.location(
                board.position(Directions.SOUTHWEST.value, selected_piece_coord)).get_occupant()

            south_heast_position = board.on_board(
                board.position(Directions.SOUTHEAST.value, selected_piece_coord)) and board.location(
                board.position(Directions.SOUTHEAST.value, selected_piece_coord)).get_occupant()

            southwest = south_west_position and south_west_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.SOUTHWEST.value,
                               board.position(Directions.SOUTHWEST.value, selected_piece_coord))) and not board.location(
                board.position(Directions.SOUTHWEST.value,
                               board.position(Directions.SOUTHWEST.value, selected_piece_coord))).get_occupant()
            southeast = south_heast_position and south_heast_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.SOUTHEAST.value,
                               board.position(Directions.SOUTHEAST.value, selected_piece_coord))) and not board.location(
                board.position(Directions.SOUTHEAST.value,
                               board.position(Directions.SOUTHEAST.value, selected_piece_coord))).get_occupant()

            if southwest:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.SOUTHWEST.value,
                                                                    board.position(Directions.SOUTHWEST.value, selected_piece_coord))))
            if southeast:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.SOUTHEAST.value,
                                                                    board.position(Directions.SOUTHEAST.value, selected_piece_coord))))

            return next_hop_movements

        else:
            south_west_position = board.on_board(
                board.position(Directions.SOUTHWEST.value, selected_piece_coord)) and board.location(
                board.position(Directions.SOUTHWEST.value, selected_piece_coord)).get_occupant()

            south_heast_position = board.on_board(
                board.position(Directions.SOUTHEAST.value, selected_piece_coord)) and board.location(
                board.position(Directions.SOUTHEAST.value, selected_piece_coord)).get_occupant()

            north_heast_position = board.on_board(
                board.position(Directions.NORTHEAST.value, selected_piece_coord)) and board.location(
                board.position(Directions.NORTHEAST.value, selected_piece_coord)).get_occupant()

            north_west_position = board.on_board(
                board.position(Directions.NORTHWEST.value, selected_piece_coord)) and board.location(
                board.position(Directions.NORTHWEST.value, selected_piece_coord)).get_occupant()

            southwest = south_west_position and south_west_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.SOUTHWEST.value,
                               board.position(Directions.SOUTHWEST.value,
                                              selected_piece_coord))) and not board.location(
                board.position(Directions.SOUTHWEST.value,
                               board.position(Directions.SOUTHWEST.value, selected_piece_coord))).get_occupant()

            southeast = south_heast_position and south_heast_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.SOUTHEAST.value,
                               board.position(Directions.SOUTHEAST.value,
                                              selected_piece_coord))) and not board.location(
                board.position(Directions.SOUTHEAST.value,
                               board.position(Directions.SOUTHEAST.value, selected_piece_coord))).get_occupant()


            northeast = north_heast_position and north_heast_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.NORTHEAST.value,
                               board.position(Directions.NORTHEAST.value, selected_piece_coord))) and not board.location(
                board.position(Directions.NORTHEAST.value,
                               board.position(Directions.NORTHEAST.value, selected_piece_coord))).get_occupant()

            northwest = north_west_position and north_west_position.get_color() != game.get_enemy_turn() and board.on_board(
                board.position(Directions.NORTHWEST.value,
                               board.position(Directions.NORTHWEST.value, selected_piece_coord))) and not board.location(
                board.position(Directions.NORTHWEST.value,
                               board.position(Directions.NORTHWEST.value, selected_piece_coord))).get_occupant()

            if southwest:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.SOUTHWEST.value,
                                                                    board.position(Directions.SOUTHWEST.value, selected_piece_coord))))
            if southeast:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.SOUTHEAST.value,
                                                                    board.position(Directions.SOUTHEAST.value, selected_piece_coord))))

            if northwest:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.NORTHWEST.value,
                                                                    board.position(Directions.NORTHWEST.value, selected_piece_coord))))
            if northeast:
                next_hop_movements.append((selected_piece_coord, board.position(Directions.NORTHEAST.value,
                                                                    board.position(Directions.NORTHEAST.value, selected_piece_coord))))

            return next_hop_movements

    def manhattan_distance(self, first_position, second_position):
        return abs(first_position[0] - second_position[0]) + abs(first_position[1] - second_position[1])

    def moves_in_player_piece_direction(self, coords_enemy_moves, coords_player_pieces):
        best_movement = None
        lower_distance = float('inf')

        for movement in coords_enemy_moves:
            for player in coords_player_pieces:
                distance = self.manhattan_distance(movement, player)
                if distance < lower_distance:
                    lower_distance = distance
                    best_movement = movement

        return best_movement

    def get_random_piece_with_approximation(self, board, game) -> (Piece, (int, int), (int, int)):
        approximation_moves = []
        player_pieces = board.get_player_pieces_position(game)

        for x in range(8):
            for y in range(8):
                piece = board.get_matrix()[x][y].get_occupant()
                if piece is not None and piece.get_color() == game.get_enemy_turn():
                    legal_moves = board.legal_moves((x, y))
                    if legal_moves:
                        approximation_moves.append(((x, y), self.moves_in_player_piece_direction(legal_moves, player_pieces), piece))

        if approximation_moves:
            random_piece = random.choice(approximation_moves)
            return random_piece[2], random_piece[1], random_piece[0]  # selected_piece, coord_to_go, coords
        else:
            return None  # Nenhuma peça tem movimentos legais


    def move_piece(self, game):
        coords_data = self.get_random_piece_with_adjacent(game.get_board(), game)

        if not coords_data:
            selected_piece, coord_to_go, coords = self.get_random_piece_with_legal_moves(game.get_board(), game)
        else:
            selected_piece, coord_to_go, coords = coords_data

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

            should_get_next_hop = self.should_get_next_hop(game, game.get_board(), game.get_selected_piece())

            if should_get_next_hop and len(should_get_next_hop) > 0:
                # faz a movimentação da peça

                game.set_selected_legal_moves([should_get_next_hop[0][1]])
                game.update()
                sleep(0.3)

                game.get_board().move_piece(game.get_selected_piece(), should_get_next_hop[0][1])
                game.get_board().remove_piece(
                    ((game.get_selected_piece()[0] + should_get_next_hop[0][1][0]) // 2,
                     (game.get_selected_piece()[1] + should_get_next_hop[0][1][1]) // 2))
