

public class Principal {

    public static void main(String [] args)
    {
        Circulo circulo = new Circulo("Mi circulo", 10, 10);
        Cuadrado cuadrado = new Cuadrado("Mi rectanuglo", 15, 15);

        System.out.println("Informacion del circulo");
        System.out.println(circulo.getNombre());
        circulo.getPosicion();


        System.out.println("Informacion del cuadrado");
        System.out.println(cuadrado.getNombre());
        cuadrado.getPosicion();

        // clonando 
        Figura figura;
        figura = circulo.clonar();
        figura.setNombre("Figura clon del circulo");

        System.out.println(figura.getNombre());
        figura.mover(10,-10);
        figura.getPosicion();;

    }
    
}
