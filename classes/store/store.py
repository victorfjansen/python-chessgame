import os
import random


class StoreFactory:
    def __init__(self) -> None:
        self.__private_store = dict()

    def _store(self, key: str, file_path: str, value: str) -> None:
        self._get_store()[key] = value
        if self._file_path_exists(file_path):
            with open(file_path, "a") as f:
                f.write(value)

    def _get_data_from_store(self, file_path: str, callback_action):
        data_dict = {}

        if self._file_path_exists(file_path):
            callback_action(file_path, data_dict)

        return data_dict

    def _delete_from_store(self, key: str) -> None:
        if self._get_store().get(key):
            self._get_store().pop(key)
        else:
            raise Exception("Was not possible to delete current data. The data was not found.")

    def _clear_all(self, file_path: str) -> None:
        self._get_store().clear()

        if self._file_path_exists(file_path):
            if os.path.getsize(file_path) > 0:
                with open(file_path, "w") as f:
                    f.truncate(0)

    def _file_path_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)

    def _has_data_on_store(self, file_path: str) -> bool:
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0

    def _get_store(self) -> dict:
        return self.__private_store
