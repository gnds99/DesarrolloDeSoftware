from asyncio import shield
from typing import List
from ListaNumeros import *
from ListaPalabras import *
from Iterador import *

ln = ListaNumeros()
lp = ListaPalabras()

ln.add(1)
ln.add(5)
ln.add(4)

lp.add("pepe")
lp.add("pecas")
lp.add("pica")
lp.add("papas")
lp.add("con un pico")

iterador = ln.iterador()

while(iterador.tieneSiguiente()):
    numero = int(iterador.siguiente())
    print(numero)
print("#####################")

iterador = lp.iterador()

while(iterador.tieneSiguiente()):
    print( iterador.siguiente() )

