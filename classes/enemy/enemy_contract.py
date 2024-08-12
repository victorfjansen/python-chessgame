from abc import ABC, abstractmethod


class EnemyContract(ABC):
    @abstractmethod
    def move_piece(self, game):
        pass
