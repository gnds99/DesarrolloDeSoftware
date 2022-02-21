from Circulo import *
from Cuadrado import *
class Principal:
    circulo = Circulo("Mi circulo", 10, 10)
    cuadrado = Cuadrado("Mi cuadrado", 15, 15)

    print("Informacion de las figuras originales")
    
    print(circulo.getNombre())
    circulo.getPosicion()

    print(cuadrado.getNombre())
    cuadrado.getPosicion()

    print("Informacion de las figuras clonadas")

    clonCirculo = circulo.clonar()
    clonCirculo.setNombre("Clon del circulo")
    clonCirculo.mover(11, 11)
    print(clonCirculo.getNombre())
    clonCirculo.getPosicion()
 

    clonCuadrado = cuadrado.clonar()
    clonCuadrado.setNombre("Clon del cuadrado")
    clonCuadrado.mover(16, 16)
    print(clonCuadrado.getNombre())
    clonCuadrado.getPosicion()


