public class App
{
    public static void main(String args[])
    {
        ListaNumeros ln = new ListaNumeros(5);
        ListaPalabras lp = new ListaPalabras();
        Iterador iterador;

        ln.add(1);
        ln.add(12);
        ln.add(14);
        ln.add(4);
        ln.add(0);
    
        lp.add("pepe");
        lp.add("pecas");
        lp.add("pica");
        lp.add("papas");
        lp.add("con un pico");

        iterador = ln.iterador();

        while(iterador.tieneSiguiente())
        {
            int numero = (int) iterador.siguiente();
            System.out.println(numero);
        }

        System.out.println(" ____________________________ ");
        iterador = lp.iterador();
        while(iterador.tieneSiguiente())
        {
            String palabra = (String) iterador.siguiente();
            System.out.println(palabra);
        }
    }
}