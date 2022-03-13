from Juego import *
from Caretaker import *
from Originator import *
nombreJuego = "Clash of Clans"

juego = Juego()
juego.setNombre(nombreJuego)
juego.setCheckPoint(1)

caretaker = Caretaker()
originator = Originator()

juego = Juego()
juego.setNombre(nombreJuego)
juego.setCheckPoint(2)

juego = Juego()
juego.setNombre(nombreJuego)
juego.setCheckPoint(3)

# guardando el punto 3
originator.setEstado(juego)
caretaker.addMemento(originator.guardar())

juego = Juego()
juego.setNombre(nombreJuego)
juego.setCheckPoint(4)

# guardando el punto 4
originator.setEstado(juego)
caretaker.addMemento(originator.guardar())

juego = Juego()
juego.setNombre(nombreJuego)
juego.setCheckPoint(5)

originator.setEstado(juego)
originator.restaurar(caretaker.getMemento(0))

juego = originator.getEstado()
print(juego.toString())


