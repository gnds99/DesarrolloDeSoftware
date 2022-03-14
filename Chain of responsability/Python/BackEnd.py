from InterfaceAyuda import *

class BackEnd(InterfaceAyuda):
    
    _TIPO_AYUDA = 3

    def __init__(self):
        self._sucesor = None

    def getAyuda(self, tipo):
        if(tipo == self._TIPO_AYUDA and self._sucesor == None):
            print("Ayuda desde el Backend")
        else:
            print("Ya no hay sucesor")      