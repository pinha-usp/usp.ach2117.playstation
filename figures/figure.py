from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def tobytes(self) -> bytes:
        pass
