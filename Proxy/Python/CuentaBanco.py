from Icuenta import *
class CuentaBanco(Icuenta):
    def retirarDinero(self, cuenta, monto):
        saldoActual = cuenta.getSaldoInicial() - monto
        cuenta.setSaldoInicial(saldoActual)
        print("Saldo actual: " + str( cuenta.getSaldoInicial()) )
        return cuenta
    
    def depositarDinero(self, cuenta, monto):
        saldoActual = cuenta.getSaldoInicial() + monto
        cuenta.setSaldoInicial(saldoActual)
        print("Saldo actual: " + str( cuenta.getSaldoInicial()) )
        return cuenta

    def mostrarSaldo(self, cuenta):
        print("Saldo actual: " + str(cuenta.getSaldoInicial()))