public class ListaNumerosIterador implements Iterador{
    private int numeros[];
    private int posicion;

    ListaNumerosIterador(int num[])
    {
        this.numeros = num;
        this.posicion = 0;
    }

    @Override
    public Object siguiente() {
        return numeros[posicion++];
    }

    @Override
    public boolean tieneSiguiente() {
        if (this.posicion < numeros.length )
        {
            return true;
        }
        else{
            return false;
        }
    }
}
