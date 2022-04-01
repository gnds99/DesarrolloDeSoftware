public class App {

    public static void main(String args[])
    {
        Caretaker caretaker = new Caretaker();
        Originator originator = new Originator();

        String nombreJuego = "Clash of clans";

        Juego juego = new Juego();
        juego.setNombre(nombreJuego);
        juego.setCheckPoint(1);
    
        juego = new Juego();
        juego.setNombre(nombreJuego);
        juego.setCheckPoint(2);
        originator.setEstado(juego); // cargar

        juego = new Juego();
        juego.setNombre(nombreJuego);
        juego.setCheckPoint(3);
        // guardando el punto 3
        originator.setEstado(juego); // cargamos el estado

        caretaker.addMemento(originator.guardar()); // guardamos el estado 0

        juego = new Juego(); // 
        juego.setNombre(nombreJuego);
        juego.setCheckPoint(4); 

        // guardando el punto 4
        originator.setEstado(juego); // cargamos el estado
        caretaker.addMemento(originator.guardar()); // guardamos el estado 1

        juego = new Juego(); // 
        juego.setNombre(nombreJuego);
        juego.setCheckPoint(5);
        originator.setEstado(juego); // cargamos el estado


        originator.restaurar(caretaker.getMemento(0));

        juego = originator.getEstado();
        System.out.println(juego);
    }

}
