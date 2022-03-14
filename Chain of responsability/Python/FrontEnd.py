from InterfaceAyuda import *

class FrontEnd(InterfaceAyuda):
    
    _TIPO_AYUDA = 1

    def __init__(self, s):
        self._sucesor = s

    def getAyuda(self, tipo):

        if(tipo == self._TIPO_AYUDA):
            print("Ayuda desde el FrontEnd")
        else:
            self._sucesor.getAyuda(tipo)        