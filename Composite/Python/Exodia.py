import this
from Carta import *
from Torso import *
from PiernaIzquierda import *
from PierndaDerecha import *
from BrazoDerecho import *
from BrazoIzquierdo import *

class Exodia(Carta):
   # _exodiaParts = []

    def __init__(self):
        self._exodiaParts = []
        self._exodiaParts.append(Torso())
        self._exodiaParts.append(PiernaDerecha())
        self._exodiaParts.append(PiernaIzquierda())
        self._exodiaParts.append(BrazoDerecho())
        self._exodiaParts.append(BrazoIzquierdo())

    def logic(self):
        print(self._exodiaParts)
        for i in range(0, 5):
            self._exodiaParts[i].logic()

