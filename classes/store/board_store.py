from classes.store.store import StoreFactory
from constants.board_store import BOARD_MATRIX_KEY


class BoardStore(StoreFactory):
    def __init__(self):
        super().__init__()
        self.__filepath = "./board_store.txt"

    def formatted_color(self, color: (int, int, int)):
        r, g, b = color
        return f"({r}-{g}-{b})"

    def store_matrix(self, matrix, game):
        game_difficulty = f"difficulty: {game.get_difficulty_level()} \n"
        self._store(BOARD_MATRIX_KEY, self.get_filepath(), game_difficulty)
        for x in range(8):
            for y in range(8):
                piece = matrix[x][y].get_occupant()
                if piece:
                    formated_string = f"x: {x}, y: {y}, color: {self.formatted_color(piece.get_color())}, king: {piece.get_king()} \n"
                    self._store(BOARD_MATRIX_KEY, self.get_filepath(), formated_string)

    def clear_stored_matrix(self):
        self._clear_all(self.get_filepath())

    def get_data_from_file(self, file_path, data_dict):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("difficulty"):
                    data_dict["difficulty"] = int(line.split(":")[1].strip())
                elif line.startswith("x:"):
                    # Parse the line to extract x, y, color, and king values
                    parts = line.split(",")
                    x = int(parts[0].split(":")[1].strip())
                    y = int(parts[1].split(":")[1].strip())
                    color = tuple(
                        map(int, parts[2].split(":")[-1].replace(" ", "").replace("(", "").replace(")", "").split("-")))
                    king = parts[-1].split(":")[1].strip() == "True"

                    info_from_file = [(x, y, color, king)]

                    if not data_dict.get("pieces_data"):
                        data_dict["pieces_data"] = info_from_file
                    else:
                        data_dict["pieces_data"] += info_from_file

    def load_game_from_file(self):
        return self._get_data_from_store(self.get_filepath(), self.get_data_from_file)

    def has_stored_data(self):
        return self._has_data_on_store(self.get_filepath())

    def get_filepath(self):
        return self.__filepath
