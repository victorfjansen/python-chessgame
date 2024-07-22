from typing import List


class BoardModel:
    def __init__(self):
        self._matrix = None

    def get_matrix(self) -> List[List[None or int]]:
        return self._matrix

    def set_matrix(self, value):
        self._matrix = value
