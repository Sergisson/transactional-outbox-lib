from abc import ABC, abstractmethod


class BaseQueueHandler(ABC):
    @abstractmethod
    def send_message(
        self,
        queue_name: str,
        message: str,
    ):
        raise NotImplemented