from abc import ABC, abstractmethod

class Iterador(ABC):
    @abstractmethod
    def siguiente(self):
        pass
    @abstractmethod
    def tieneSiguiente(self):
        pass