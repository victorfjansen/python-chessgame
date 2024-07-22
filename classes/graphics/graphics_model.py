import pygame


class GraphicsModel:
    def __init__(self):
        self._text_font_obj = None
        self._text_rect_obj = None
        self._text_surface_obj = None
        self._caption = "Damas by Victorfjansen"

        self._fps = 60
        self._clock = pygame.time.Clock()

        self._window_size = 600
        self._screen = pygame.display.set_mode((self.get_window_size(), self.get_window_size()))
        self._background = pygame.image.load('assets/board.png')
        self._scaledbackground = pygame.transform.scale(self.get_background(),
                                                         (self.get_window_size(), self.get_window_size()))

        self._square_size = self.get_window_size() >> 3
        self._piece_size = self.get_square_size() // 2

        self._message = False

    def get_caption(self):
        return self._caption

    def get_fps(self):
        return self._fps

    def get_clock(self):
        return self._clock

    def get_window_size(self):
        return self._window_size

    def get_screen(self):
        return self._screen

    def get_background(self):
        return self._background

    def get_scaledbackground(self):
        return self._scaledbackground

    def get_square_size(self):
        return self._square_size

    def get_piece_size(self):
        return self._piece_size

    def get_text_rect_obj(self):
        return self._text_rect_obj

    def set_text_rect_obj(self, value):
        self._text_rect_obj = value

    def get_font_obj(self):
        return self._text_font_obj

    def set_font_obj(self, value):
        self._text_font_obj = value

    def get_text_surface_obj(self):
        return self._text_surface_obj

    def set_text_surface_obj(self, value):
        self._text_surface_obj = value

    def set_message(self, value):
        self._message = value

    def get_message(self):
        return self._message
