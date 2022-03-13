from abc import abstractmethod
from re import X
from Figura import *

class Cuadrado(Figura):

    def __init__(self, nombre, x, y):

        self._nombre = nombre
        self._x = x
        self._y = y

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    def mover(self, x, y):
        self._x = x
        self._y = y

    def getPosicion(self):
        print(self._x)
        print(self._y)
    
    def clonar(self):
        figura = Cuadrado(self._nombre,self._x, self._y )
        return figura