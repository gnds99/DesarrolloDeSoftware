from decimal import Clamped
from Iterador import *

class ListaPalabrasIterador(Iterador):
    
    def __init__(self, p1, p2, p3, p4, p5):
        self._palabra1 = p1
        self._palabra2 = p2
        self._palabra3 = p3 
        self._palabra4 = p4 
        self._palabra5 = p5
        self._posicion = 0
    
    def siguiente(self):
        p = ''
        if self._posicion == 0:
            p = self._palabra1
        if self._posicion == 1:
            p =  self._palabra2        
        if self._posicion == 2:
            p =  self._palabra3
        if self._posicion == 3:
            p = self._palabra4
        if self._posicion == 4:
            p =  self._palabra5

        self._posicion += 1
        return p
    def tieneSiguiente(self):
        
        if self._posicion < 5:
            return True
        else:
            return False