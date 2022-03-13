from ListaNumerosIterador import *

class ListaNumeros:
    def __init__(self):
        self._posicion = 0
        self._numeros = []
    
    def add(self, numero):
        self._numeros.append(numero)

    def iterador(self):
        return ListaNumerosIterado(self._numeros)  

