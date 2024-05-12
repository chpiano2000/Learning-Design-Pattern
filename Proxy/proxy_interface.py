from abc import ABC, abstractmethod


class Personnel(ABC):
    @abstractmethod
    def handle_request(self, offer) -> None:
        pass
