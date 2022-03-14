from BackEnd import *
from FrontEnd import *
from Middle import *

backend  = BackEnd()
middle = Middle(backend)
frontEnd = FrontEnd(middle)

frontEnd.getAyuda(1)

