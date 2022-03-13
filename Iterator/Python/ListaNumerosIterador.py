from Iterador import *

class ListaNumerosIterado(Iterador):

    def __init__(self, numeros):
        self._numeros = numeros
        self._posicion = 0
    
    def siguiente(self):
        valor = self._numeros[self._posicion]
        self._posicion += 1
        return valor
    
    def tieneSiguiente(self):
        if  self._posicion < len(self._numeros):
            return True
        else:
            return False
        

    