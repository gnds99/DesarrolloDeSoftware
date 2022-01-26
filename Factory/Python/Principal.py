import ShapeFactory

if __name__ == '__main__':
    mi_shape = ShapeFactory.shapeFactory()

    rectangulo = mi_shape.get_Shape('r', 4)
    rectangulo.getLados()
    rectangulo.draw()
    cuadrado = mi_shape.get_Shape('s', 2)   
    cuadrado.getLados()
    cuadrado.draw()


