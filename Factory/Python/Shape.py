"""
Clase que define una forma
"""

class shape(object):

    numLados = 0
    def __init__(self, numLados):
        print("figura construida")
        self.numLado = numLados

    def draw(self):
        print("Imprimiendo figura")

    def getLados(self):
        print(self.numLados)