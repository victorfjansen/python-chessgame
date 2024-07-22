from typing import List


class BoardModel:
    def __init__(self):
        self.__matrix = None

    def get_matrix(self) -> List[List[None or int]]:
        return self.__matrix

    def set_matrix(self, value):
        self.__matrix = value
