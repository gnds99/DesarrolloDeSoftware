from Rectangle import rectangle
from Square import square


class shapeFactory(object):


    def get_Shape(self, figura, numlados):
        if(figura == 'r'):
            return rectangle(numlados)
        elif(figura == 's'):
            return square(numlados)

