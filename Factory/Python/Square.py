
from Shape import shape

class square(shape):

    """ Esta clase hereda de la super clase Shape """

    def __init__(self, numLados):
        print("Cuadrado")
        self.numLados = numLados
    
    def draw(self):
        for i in range(0, self.numLados):
            for j in range(0, self.numLados):
                print("* ", end="")
            print(" ")
        