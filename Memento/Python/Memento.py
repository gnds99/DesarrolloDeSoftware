class Memento:

    def __init__(self, estado):
        self._estado = estado
    
    def getEstado(self):
        return self._estado