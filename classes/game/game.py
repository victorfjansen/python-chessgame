import sys
import pygame

from classes.enemy.easy_enemy import EasyEnemy
from classes.enemy.medium_enemy import MediumEnemy
from classes.game.game_contract import GameContract
from classes.game.game_model import GameModel
from classes.piece.piece import Piece
from constants.colors import COLORS
from constants.difficulty import DifficultyLevel
from time import sleep


class Game(GameModel, GameContract):
    def __init__(self):
        pygame.font.init()
        GameModel.__init__(self)

    def setup_enemy(self):
        if self.get_difficulty_level() == DifficultyLevel.EASY.value:
            self.set_enemy(EasyEnemy())
        elif self.get_difficulty_level() == DifficultyLevel.MEDIUM.value:
            self.set_enemy(MediumEnemy())

    def setup(self):
        self.get_graphics().setup_window()
        if not self.get_difficulty_level() == DifficultyLevel.LOCAL.value:
            self.setup_enemy()

    def event_loop(self):

        # pega posição do mouse e peça respectiva
        self.set_mouse_pos(self.get_graphics().board_coords(pygame.mouse.get_pos()))

        # pega movimentos disponíveis para peça caso exista
        if self.get_selected_piece() is not None:
            self.set_selected_legal_moves(self.get_board().legal_moves(self.get_selected_piece(), self.get_hop()))

        for event in pygame.event.get():

            # encerra o jogo caso o usuário saia
            if event.type == pygame.QUIT:
                self.terminate_game()

            if self.get_turn() == self.get_enemy_turn() and not self.get_difficulty_level() == DifficultyLevel.LOCAL.value:
                if not self.get_end_game():
                    self.get_enemy().move_piece(self)
                    self.end_turn()

            # verifica se o evento é de clique
            if event.type == pygame.MOUSEBUTTONDOWN:

                # verifica se uma peça foi capturada. Se não:
                if not self.get_hop():
                    # faz a seleção da peça
                    if (self.get_board().location(self.get_mouse_pos()).get_occupant() is not None and
                            self.get_board().location(self.get_mouse_pos()).get_occupant().get_color() == self.get_turn()):
                        self.set_selected_piece(self.get_mouse_pos())

                    # verifica se a peça selecionada e o movimento é um movimento que se possa fazer
                    elif self.get_selected_piece() is not None and self.get_mouse_pos() in self.get_board().legal_moves(
                            self.get_selected_piece()):
                        self.get_board().move_piece(self.get_selected_piece(), self.get_mouse_pos())

                        # se a posição selecionada não está adjacente (diagonal) da referência anterior,
                        # significa que uma peça foi capturada e precisa ser removida do board
                        if self.get_mouse_pos() not in self.get_board().adjacent(self.get_selected_piece()):
                            # faz uma media e pega a peça do meio, a partir da referência e da nova peça
                            self.get_board().remove_piece((
                                (self.get_selected_piece()[0] + self.get_mouse_pos()[0]) // 2,
                                (self.get_selected_piece()[1] + self.get_mouse_pos()[1]) // 2))

                            # seta a captura como true
                            self.set_hop(True)
                            self.set_selected_piece(self.get_mouse_pos())

                        # se não houver, encerra o turno
                        else:
                            self.end_turn()

                if self.get_hop():
                    # se houver uma peça capturada e ainda houver movimentos "legais"
                    if (self.get_selected_piece() is not None and self.get_mouse_pos() in
                            self.get_board().legal_moves(self.get_selected_piece(), self.get_hop())):
                        # faz a movimentação da peça
                        self.get_board().move_piece(self.get_selected_piece(), self.get_mouse_pos())
                        self.get_board().remove_piece(
                            ((self.get_selected_piece()[0] + self.get_mouse_pos()[0]) // 2,
                             (self.get_selected_piece()[1] + self.get_mouse_pos()[1]) // 2))

                    # verifica se não tem mais movimentos possíveis e encerra
                    if not self.get_board().legal_moves(self.get_mouse_pos(), self.get_hop()):
                        self.end_turn()

                    # refaz a nova lógica
                    else:
                        self.set_selected_piece(self.get_mouse_pos())

    def update(self):
        # faz o update do jogo a partir dos novos movimentos
        self.get_graphics().update_display(self.get_board(), self.get_selected_legal_moves(), self.get_selected_piece())

    def terminate_game(self):
        if not self.get_end_game():
            self.get_board_store().store_matrix(self.get_board().get_matrix(), self)
        else:
            self.get_board_store().clear_stored_matrix()
        pygame.quit()
        sys.exit()

    def main(self):
        self.get_main_menu().setup_menu(self)

    def clean_board_store(self):
        self.get_board_store().clear_stored_matrix()

    def load_stored_game(self):
        saved_game_dict = self.get_board_store().load_game_from_file()

        if not len(saved_game_dict):
            return

        self.set_difficulty_level("", saved_game_dict['difficulty'])

        for x in range(8):
            for y in range(8):
                self.get_board().remove_piece((x, y))

        for piece_data in saved_game_dict['pieces_data']:
            x = piece_data[0]
            y = piece_data[1]
            self.get_board().get_matrix()[x][y].set_occupant(Piece(piece_data[2], piece_data[-1]))

        self.init_game_main_loop()

    def init_game_main_loop(self):
        # seta o window e interface gráfica
        self.setup()
        self.clean_board_store()

        # loop principal
        while True:
            self.event_loop()
            self.update()

    def end_turn(self):
        if self.get_turn() == COLORS.BLUE.value:
            self.set_turn(COLORS.RED.value)
        else:
            self.set_turn(COLORS.BLUE.value)

        self.set_selected_piece(None)
        self.set_selected_legal_moves([])
        self.set_hop(False)

        if self.check_for_endgame():
            if self.get_turn() == COLORS.BLUE.value:
                self.get_graphics().draw_message("VERMELHO GANHOU!")
            else:
                self.get_graphics().draw_message("CINZA GANHOU!")

    def check_for_endgame(self):
        board = self.get_board()
        turn_color = self.get_turn()

        for x in range(8):
            for y in range(8):
                location = board.location((x, y))
                occupant = location.get_occupant()

                if occupant is not None and occupant.get_color() == turn_color:
                    if board.legal_moves((x, y)):
                        return False

        self.set_end_game(True)
        return True
