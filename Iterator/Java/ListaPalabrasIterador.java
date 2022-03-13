public class ListaPalabrasIterador implements Iterador
{
    private String palabra1, palabra2, palabra3, palabra4, palabra5;
    private int posicion;

    ListaPalabrasIterador(String p1, String p2, String p3, String p4, String p5)
    {
        this.palabra1 = p1;
        this.palabra2 = p2;
        this.palabra3 = p3;
        this.palabra4 = p4;
        this.palabra5 = p5;
        this.posicion = 0;
    }
    @Override
    public Object siguiente() {
        switch(this.posicion++)
        {
            case 0:
                return this.palabra1;
                
            case 1:
                return this.palabra2;
                
            case 2:
                return this.palabra3;
                
            case 3:
                return this.palabra4;
                
            case 4:
                return this.palabra5;
        }
        return null;
    }

    @Override
    public boolean tieneSiguiente() {
        if(this.posicion < 5)
        {
            return true;
        }else{
            return false;
        }
    }
    
}
