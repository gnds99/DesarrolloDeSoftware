from abc import ABC, abstractclassmethod

class Figura(ABC):
    @abstractclassmethod
    def setNombre(self, nombre):
        pass
   
    @abstractclassmethod
    def getNombre(self):
        pass
    
    @abstractclassmethod
    def mover(self, x, y):
        pass

    @abstractclassmethod
    def getPosicion(self):
        pass
    
    @abstractclassmethod
    def clonar(self):
        pass