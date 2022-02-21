class Pizza:

    _masa = " "
    _relleno = " "
    _salsa = " "
    
    def setMasa(self, masa):
        self._masa = masa
    
    def setRelleno(self, relleno):
        self._relleno = relleno
    
    def setSalsa(self,salsa):
        self._salsa = salsa

    def dataPizza(self):
        print("Pizza: " + self._masa + self._relleno + self._salsa)

