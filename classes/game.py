import sys
import pygame
from classes.board.board import Board
from classes.graphics.graphics import Graphics
from constants.colors import COLORS


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()

        #primeiro turno
        self.turn = COLORS.BLUE.value

        # localização do board
        self.selected_piece = None

        #verifica se uma peça foi capturada
        self.hop = False
        self.selected_legal_moves = []

    def setup(self):
        self.graphics.setup_window()

    def event_loop(self):

        # pega posição do mouse e peça respectiva
        self.mouse_pos = self.graphics.board_coords(pygame.mouse.get_pos())

        # pega movimentos disponíveis para peça caso exista
        if self.selected_piece != None:
            self.selected_legal_moves = self.board.legal_moves(self.selected_piece, self.hop)

        for event in pygame.event.get():

            # encerra o jogo caso o usuário saia
            if event.type == pygame.QUIT:
                self.terminate_game()

            # verifica se o evento é de clique
            if event.type == pygame.MOUSEBUTTONDOWN:

                # verifica se uma peça foi capturada. Se não:
                if not self.hop:

                    # faz a seleção da peça
                    if self.board.location(self.mouse_pos).occupant != None and self.board.location(
                            self.mouse_pos).occupant.color == self.turn:
                        self.selected_piece = self.mouse_pos

                    # verifica se a peça selecionada e o movimento é um movimento que se possa fazer
                    elif self.selected_piece is not None and self.mouse_pos in self.board.legal_moves(
                            self.selected_piece):

                        self.board.move_piece(self.selected_piece, self.mouse_pos)

                        # se a posição selecionada não está adjacente (diagonal) da referência anterior,
                        # significa que uma peça foi capturada e precisa ser removida do board
                        if self.mouse_pos not in self.board.adjacent(self.selected_piece):
                            # faz uma media e pega a peça do meio, a partir da referência e da nova peça
                            self.board.remove_piece(((self.selected_piece[0] + self.mouse_pos[0]) // 2,
                                                     (self.selected_piece[1] + self.mouse_pos[1]) // 2))

                            # seta a captura como true
                            self.hop = True
                            self.selected_piece = self.mouse_pos

                        # se não houver, encerra o turno
                        else:
                            self.end_turn()

                if self.hop:
                    # se houver uma peça capturada e ainda houver movimentos "legais"
                    if self.selected_piece is not None and self.mouse_pos in self.board.legal_moves(self.selected_piece,
                                                                                                    self.hop):
                        # faz a movimentação da peça
                        self.board.move_piece(self.selected_piece, self.mouse_pos)
                        self.board.remove_piece(((self.selected_piece[0] + self.mouse_pos[0]) // 2,
                                                 (self.selected_piece[1] + self.mouse_pos[1]) // 2))

                    # verifica se não tem mais movimentos possíveis e encerra
                    if not self.board.legal_moves(self.mouse_pos, self.hop):
                        self.end_turn()

                    # refaz a nova lógica
                    else:
                        self.selected_piece = self.mouse_pos

    def update(self):
        # faz o update do jogo a partir dos novos movimentos
        self.graphics.update_display(self.board, self.selected_legal_moves, self.selected_piece)

    def terminate_game(self):
        # Quita e termina o jogo
        pygame.quit()
        sys.exit()

    def main(self):
        # seta o window e interface gráfica
        self.setup()

        # loop principal
        while True:
            self.event_loop()
            self.update()

    def end_turn(self):
        if self.turn == COLORS.BLUE.value:
            self.turn = COLORS.RED.value
        else:
            self.turn = COLORS.BLUE.value

        self.selected_piece = None
        self.selected_legal_moves = []
        self.hop = False

        if self.check_for_endgame():
            if self.turn == COLORS.BLUE.value:
                self.graphics.draw_message("Vermelho ganhou")
            else:
                self.graphics.draw_message("Azul Ganhou!")

    def check_for_endgame(self):
        for x in range(8):
            for y in range(8):
                if self.board.location((x, y)).color == COLORS.BLACK.value and self.board.location(
                        (x, y)).occupant is not None and self.board.location((x, y)).occupant.color == self.turn:
                    if self.board.legal_moves((x, y)):
                        return False

        return True
