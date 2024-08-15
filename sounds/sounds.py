import pygame.mixer
import os


class StaticSounds:
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def initialize_mixer():
        pygame.mixer.init()

    @staticmethod
    def play_movement_sound():
        file_path = os.path.join(StaticSounds.sourceFileDir, 'movement.mp3')
        movement_sound = pygame.mixer.Sound(file_path)
        movement_sound.play()

    @staticmethod
    def play_promote_piece_sound():
        file_path = os.path.join(StaticSounds.sourceFileDir, 'promote.mp3')
        promote_piece = pygame.mixer.Sound(file_path)
        promote_piece.play()
