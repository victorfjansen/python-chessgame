from abc import ABC, abstractmethod


class MenuContract(ABC):
    @abstractmethod
    def setup_menu(self, game):
        pass
