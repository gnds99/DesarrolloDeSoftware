from Memento import *
class Originator:

    def __init__(self):
        self._estado = ''

    def setEstado(self, estado):
        self._estado = estado
    
    def getEstado(self):
        return self._estado
    
    def guardar(self):
        return Memento(self._estado)

    def restaurar(self, m):
        self._estado = m.getEstado()