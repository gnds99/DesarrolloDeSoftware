public class ListaNumeros{
    private int numeros[];
    private int posicion;

    ListaNumeros(int x)
    {
        this.numeros = new int[x];
        this.posicion = 0;
    }

    public void add(int numero)
    {
        this.numeros[this.posicion++] = numero;
    }

    public ListaNumerosIterador iterador()
    {
        return new ListaNumerosIterador(this.numeros);
    }

}