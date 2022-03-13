class Juego:
    def __init__(self):
        self._nombre = ''
        self._checkPoint = 0
    
    def getCheckPoint(self):
        return self._checkPoint
    
    def setCheckPoint(self, checkPoint):
        self._checkPoint = checkPoint
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def toString(self):
        return "Juego [nombre " + self._nombre + " checkpoint = " + str(self._checkPoint) + "]"