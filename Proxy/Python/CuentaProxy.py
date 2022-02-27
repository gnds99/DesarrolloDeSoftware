from Icuenta import *
from CuentaBanco import *

class CuentaProxy(Icuenta):

    _cuentaReal = None
    
    def __init__(self, cuentaReal):
        print("ME he creado")
        self._cuentaReal = cuentaReal

    def retirarDinero(self, cuenta, monto):
        if(self._cuentaReal == None ):
            print("Entre 1 ")
            self._cuentaReal = CuentaBanco()
            return self._cuentaReal.retirarDinero(cuenta, monto)
        else:
            print("entre dos")
            return self._cuentaReal.retirarDinero(cuenta, monto)

    def depositarDinero(self, cuenta, monto):
        if(self._cuentaReal == None):
            "entre 3"
            self._cuentaReal = CuentaBanco()
            return self._cuentaReal.depositarDinero(cuenta, monto)
        else:
            "entre 4"
            return self._cuentaReal.depositarDinero(cuenta, monto)
    
    def mostrarSaldo(self, cuenta):
        if(self._cuentaReal == None):
            self._cuentaReal = CuentaBanco()
            return self._cuentaReal.mostrarSaldo(cuenta)
        else:
            self._cuentaReal.mostrarSaldo(cuenta)