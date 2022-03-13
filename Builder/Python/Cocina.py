from PizzaBuilder import *
class Cocina:

    _pizzaBuilder = None

    def setPizzaBuilder(self, pb):
        self._pizzaBuilder = pb
    
    def getPizza(self):
        return self._pizzaBuilder.getPizza()
    
    def constuirPizza(self):
        self._pizzaBuilder.crearNuevaPizza()
        self._pizzaBuilder.buildMasa()
        self._pizzaBuilder.buildRelleno()
        self._pizzaBuilder.buildSalsa()  