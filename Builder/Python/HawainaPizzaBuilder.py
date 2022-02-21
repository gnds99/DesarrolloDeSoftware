from PizzaBuilder import *

class HawainaPizzaBuilder(PizzaBuilder):
    
    def buildMasa(self):
        self._pizza.setMasa("suave")
        
    def buildSalsa(self):
        self._pizza.setSalsa(" dulce")

    def buildRelleno(self):
        self._pizza.setRelleno(" Piña")
