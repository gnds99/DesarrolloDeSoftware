from Shape import shape

class rectangle(shape):

    """ Esta clase hereda de la super clase Shape """

    def __init__(self, numLados):
        print("Rectangulo")
        self.numLados = numLados

    def draw(self):
        for i in range(0, self.numLados):
            for j in range(0, self.numLados*2):
                print("* ", end="")
            print(" ")
