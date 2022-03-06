from Circle import *
from ShapeFactory import *
import random

def getRandomColor():
    color = ''
    valor = random.randrange(6)
    if(valor == 1):
        color = "Red"
    if(valor == 2):
        color = "Green"   
    if(valor == 3):
        color = "Blue"
    if(valor == 4):
        color = "White"
    if(valor == 5):
        color = "Black"
    return color

def getRandomX():
    return random.randrange(100)

def getRandomY():
    return random.randrange(100)

for i in range(0,20):
    print("Entre")
    print(getRandomColor())

    circle = ShapeFactory.getCircle(self, getRandomColor())
    circle.setX(getRandomX())
    circle.setY(getRandomY())
    circle.setRadius(100)
    circle.draw()

