import pygame

from classes.graphics.graphics_contract import GraphicsContract
from classes.graphics.graphics_model import GraphicsModel
from constants.colors import COLORS


class Graphics(GraphicsModel, GraphicsContract):
    def __init__(self):
        GraphicsModel.__init__(self)

    def setup_window(self):
        #Inicializa a window 
        pygame.display.set_caption(self.get_caption())

    def update_display(self, board, legal_moves, selected_piece):
        # faz o update da tela, colcando os movimentos possíveis
        self.get_screen().blit(self.get_scaledbackground(), (0, 0))

        self.highlight_squares(legal_moves, selected_piece)
        self.draw_board_pieces(board)

        if self.get_message():
            self.get_screen().blit(self.get_text_surface_obj(), self.get_text_rect_obj())

        pygame.display.update()
        self.get_clock().tick(self.get_fps())

    def draw_board_pieces(self, board):
        # Desenha as peças no display
        red_pawn_image = "assets/pieces/red-pawn.png"
        red_pawn_image = pygame.transform.scale(pygame.image.load(red_pawn_image),
                                                (self.get_square_size(), self.get_square_size()))

        black_pawn_image = "assets/pieces/black-pawn.png"
        black_pawn_image = pygame.transform.scale(pygame.image.load(black_pawn_image),
                                                  (self.get_square_size(), self.get_square_size()))
        for x in range(8):
            for y in range(8):
                current_piece = board.get_matrix()[x][y].get_occupant()
                if current_piece is not None:
                    try:
                        self.get_screen().blit(
                            black_pawn_image if current_piece.get_color() == COLORS.BLUE.value else red_pawn_image,
                            self.pixel_coords((x - 0.5, y - 0.5)))

                    except:
                        pygame.draw.circle(self.get_screen(), board.get_matrix()[x][y].get_occupant().get_color(),
                                           self.pixel_coords((x, y)), self.get_piece_size())

                    if board.location((x, y)).get_occupant().get_king():
                        try:
                            pawn_image = "assets/pieces/black-king.png" if current_piece.get_color() == COLORS.BLUE.value \
                                else "assets/pieces/red-king.png"
                            pawn_image = pygame.transform.scale(pygame.image.load(pawn_image),
                                                                (self.get_square_size(), self.get_square_size()))
                            self.get_screen().blit(pawn_image, self.pixel_coords((x - 0.5, y - 0.5)))

                        except:
                            pygame.draw.circle(self.get_screen(), COLORS.GOLD.value, self.pixel_coords((x, y)),
                                               int(self.get_piece_size() / 1.7), self.get_piece_size() >> 2)

    def pixel_coords(self, board_coords):
        #pega a tupla "posições" dos quadrados na tela
        return (board_coords[0] * self.get_square_size() +
                self.get_piece_size(), board_coords[1] * self.get_square_size() + self.get_piece_size())

    def board_coords(self, pixel):
        # retorna as coordenadas dos quadrados
        return pixel[0] // self.get_square_size(), pixel[1] // self.get_square_size()

    def highlight_squares(self, squares, origin):
        for square in squares:
            pygame.draw.rect(self.get_screen(), COLORS.HIGH.value,
                             (square[0] * self.get_square_size(), square[1] * self.get_square_size(),
                              self.get_square_size(), self.get_square_size()))

        if origin is not None:
            pygame.draw.rect(self.get_screen(), COLORS.HIGH.value, (
                origin[0] * self.get_square_size(), origin[1] * self.get_square_size(),
                self.get_square_size(), self.get_square_size()))

    def draw_message(self, message):
        self.set_message(True)
        self.set_font_obj(pygame.font.Font('freesansbold.ttf', 44))
        self.set_text_surface_obj(self.get_font_obj().render(message, True, COLORS.RED.value, COLORS.WHITE.value))
        self.set_text_rect_obj(self.get_text_surface_obj().get_rect())
        self.get_text_rect_obj().center = (self.get_window_size() >> 1, self.get_window_size() >> 1)
