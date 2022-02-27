class Cuenta:

    def __init__(self, idcuenta, usuario, saldoInicial):
        self._idCuenta = idcuenta
        self._usuario = usuario
        self._saldoInicial = saldoInicial
    
    # Getters
    def getCuenta(self):
        return self._idCuenta
    
    def getUsuario(self):
        return self._usuario
        
    def getSaldoInicial(self):
        return self._saldoInicial
    
    # Setters
    def setIdCuenta(self, idCuenta):
        self._idCuenta = idCuenta
    def setUsuario(self, usuario):
        self._usuario = usuario
    def setSaldoInicial(self, saldoInicial):
        self._saldoInicial = saldoInicial