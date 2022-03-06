from Shape import *

class Circle(Shape):

    _x = 0
    _y = 0
    _radius = 0

    def __init__(self, color):
        self._color = color

    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y

    def setRadius(self, radius):
        self._radius = radius

    def draw():
        print("Circle: Draw() [Color: " + str(self._color) + ", x : " + str(self._x) + ", y : " + str(self._y) + ", radius : " + str(self._radius))
