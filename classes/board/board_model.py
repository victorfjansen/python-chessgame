from typing import List

from classes.store.board_store import BoardStore


class BoardModel:
    def __init__(self):
        self.__matrix = None
        self.__board_store = BoardStore()

    def get_matrix(self) -> List[List[None or int]]:
        return self.__matrix

    def set_matrix(self, value):
        self.__matrix = value

    def get_board_store(self):
        return self.__board_store
