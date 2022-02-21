from abc import ABC, abstractmethod
from Pizza import *

class PizzaBuilder(ABC):

    _pizza = None

    def getPizza(self):
        return self._pizza
    
    def crearNuevaPizza(self):
        self._pizza = Pizza()

    @abstractmethod
    def buildMasa(self):
        pass
    @abstractmethod
    def buildSalsa(self):
        pass
    @abstractmethod
    def buildRelleno(self):
        pass