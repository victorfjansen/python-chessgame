import pygame
import pygame_menu

def set_difficulty(value, difficulty):
    # Do the job here !
    print(difficulty)
        
class MainMenu():
    def __init__(self):
        pygame.init()
        self.__surface = pygame.display.set_mode((600, 600))

    def set_difficulty(value, difficulty):
        # Do the job here !
        print(difficulty)
        

    def start_the_game():
        # Do the job here !
        print("a")

    def setup_menu(self, game):
        menu = pygame_menu.Menu('Selecione seu modo de jogo! ', 600, 600,
                        theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Jogar!', game.init_game_main_loop)
        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.add.selector('Nível :', [('Fácil', 1), ('Difícil', 2)], onchange=MainMenu.set_difficulty)

        menu.mainloop(self.__surface)