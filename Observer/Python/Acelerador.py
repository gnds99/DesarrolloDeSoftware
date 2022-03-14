from SujetoObservable import *
from Observador import *

class Acelerador(SujetoObservable):
    def __init__(self):
        self._observers = []
    
    def pisarAcelerador(self):
        self.notificar()
    
    def attach(self, o):
        self._observers.append(o)
    
    def notificar(self):
        for o in self._observers:
            o.update()