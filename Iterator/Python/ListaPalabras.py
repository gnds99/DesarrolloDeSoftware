from ListaPalabrasIterador import *

class ListaPalabras:
    
    def __init__(self):
        self._posicion = 0
        self._palabra1 = '' 
        self._palabra2 = '' 
        self._palabra3 = '' 
        self._palabra4 = ''
        self._palabra5 = '' 
        self._posicion = 0
    
    def add(self, p):

        if self._posicion == 0:
            self._palabra1 = p

        if self._posicion == 1:
            self._palabra2 = p
        
        if self._posicion == 2:
            self._palabra3 = p
        
        if self._posicion == 3:
            self._palabra4 = p
        
        if self._posicion == 4:
            self._palabra5 = p
        
        self._posicion += 1
    
    def iterador(self):
        return ListaPalabrasIterador(self._palabra1, self._palabra2, self._palabra3, self._palabra4, self._palabra5)
        

 