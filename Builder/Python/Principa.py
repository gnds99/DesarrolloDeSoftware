from MexicanaPizzaBuilder import *
from Cocina import *
from HawainaPizzaBuilder import *
from Pizza import *

cocina = Cocina()
hawai = HawainaPizzaBuilder()
mexican = MexicanaPizzaBuilder()

cocina.setPizzaBuilder(hawai)
cocina.constuirPizza()

pizza = cocina.getPizza()
pizza.dataPizza()

cocina.setPizzaBuilder(mexican)
cocina.constuirPizza()
pizza2 = cocina.getPizza()
pizza2.dataPizza()