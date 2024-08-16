from abc import ABC, abstractmethod


class GameContract(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def event_loop(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def terminate_game(self):
        pass

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def end_turn(self):
        pass

    @abstractmethod
    def check_for_endgame(self):
        pass

    @abstractmethod
    def clean_board_store(self):
        pass

    @abstractmethod
    def load_stored_game():
        pass

    @abstractmethod
    def setup_enemy():
        pass