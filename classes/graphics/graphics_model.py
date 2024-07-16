import pygame


class GraphicsModel:
    def __init__(self):
        self.__text_font_obj = None
        self.__text_rect_obj = None
        self.__font_obj = None
        self.__text_surface_obj = None
        self.__caption = "Damas by Victorfjansen"

        self.__fps = 60
        self.__clock = pygame.time.Clock()

        self.__window_size = 1000
        self.__screen = pygame.display.set_mode((self.get_window_size(), self.get_window_size()))
        self.__background = pygame.image.load('assets/board.png')
        self.__scaledbackground = pygame.transform.scale(self.get_background(),
                                                         (self.get_window_size(), self.get_window_size()))

        self.__square_size = self.get_window_size() >> 3
        self.__piece_size = self.get_square_size() // 2

        self.__message = False

    def get_caption(self):
        return self.__caption

    def get_fps(self):
        return self.__fps

    def get_clock(self):
        return self.__clock

    def get_window_size(self):
        return self.__window_size

    def get_screen(self):
        return self.__screen

    def get_background(self):
        return self.__background

    def get_scaledbackground(self):
        return self.__scaledbackground

    def get_square_size(self):
        return self.__square_size

    def get_piece_size(self):
        return self.__piece_size

    def get_text_rect_obj(self):
        return self.__text_rect_obj

    def set_text_rect_obj(self, value):
        self.__text_rect_obj = value

    def get_font_obj(self):
        return self.__font_obj

    def set_font_obj(self, value):
        self.__text_font_obj = value

    def get_text_surface_obj(self):
        return self.__text_surface_obj

    def set_text_surface_obj(self, value):
        self.__text_surface_obj = value

    def set_message(self, value):
        self.__message = value

    def get_message(self):
        return self.__message
