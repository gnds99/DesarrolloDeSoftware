from curses.textpad import rectangle
from Circle import *
from Rectangle import *
from Square import *

class ShapeMaker:

    def __init__(self):
        self._circle = Circle()
        self._rectangle = Rectangle()
        self._square = Square()
    
    def drawCircle(self):
        self._circle.draw()
    
    def drawRectangle(self):
        self._rectangle.draw()

    def drawSquare(self):
        self._square.draw()

    
