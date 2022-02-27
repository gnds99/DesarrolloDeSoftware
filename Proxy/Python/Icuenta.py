from abc import ABC, abstractmethod

class Icuenta(ABC):
    @abstractmethod
    def retirarDinero(self,cuenta, monto):
        pass
    @abstractmethod
    def depositarDinero(self, cuenta, monto):
        pass
    @abstractmethod
    def mostrarSaldo(self, cuenta):
        pass
    