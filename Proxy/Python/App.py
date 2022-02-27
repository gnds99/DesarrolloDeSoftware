from Cuenta import *
from Icuenta import *
from CuentaProxy import *
from CuentaBanco import *
debito = Cuenta(1, "noe", 1000)

cuenta = CuentaProxy(CuentaBanco())
debito = cuenta.retirarDinero(debito, 300)
debito = cuenta.depositarDinero(debito, 500)
cuenta.mostrarSaldo(debito)