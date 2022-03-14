from Motor import *
from Acelerador import *

v8 = Motor()
acelerador = Acelerador()

acelerador.attach(v8)
acelerador.pisarAcelerador()