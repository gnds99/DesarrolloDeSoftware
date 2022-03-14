from InterfaceAyuda import *

class Middle(InterfaceAyuda):
    
    _TIPO_AYUDA = 2

    def __init__(self, s):
        self._sucesor = s

    def getAyuda(self, tipo):
        if(tipo == self._TIPO_AYUDA):
            print("Ayuda desde el Middle")
        else:
            self._sucesor.getAyuda(tipo)        