from abc import ABC, abstractmethod

class SujetoObservable(ABC):
    @abstractmethod
    def notificar(self):
        pass