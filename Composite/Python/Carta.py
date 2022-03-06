from abc import ABC, abstractmethod

class Carta(ABC):
    @abstractmethod
    def logic(self):
        pass
