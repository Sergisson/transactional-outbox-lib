from abc import ABC, abstractmethod


class BaseDBHandler(ABC):
    @abstractmethod
    def save_changes(
        self,
        database_table: str,
        # TODO какой тут интерфейс? Какое поле и какое велью?
    ):
        raise NotImplemented



