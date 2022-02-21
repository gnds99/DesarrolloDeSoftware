from PizzaBuilder import *

class MexicanaPizzaBuilder(PizzaBuilder):
    
    def buildMasa(self):
        self._pizza.setMasa("gruesa")
        
    def buildSalsa(self):
        self._pizza.setSalsa(" Extra picante")

    def buildRelleno(self):
        self._pizza.setRelleno(" bolitas de carne")
