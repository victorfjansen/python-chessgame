from abc import ABC, abstractmethod


class MenuContract(ABC):
    @abstractmethod
    def setup_menu(self, game):
        pass

    @abstractmethod
    def has_data_on_store(game):
        pass
