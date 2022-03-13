
public class ListaPalabras {
    private String palabra1, palabra2, palabra3, palabra4, palabra5;
    private int posicion;

    ListaPalabras()
    {
        this.posicion = 0;
    }

    public void add(String p)
    {
        switch(this.posicion)
        {
            case 0:
                this.palabra1 = p;
                break;
            case 1:
                this.palabra2 = p;
                break;
            case 2:
                this.palabra3 = p;
                break;
            case 3:
                this.palabra4 = p;
                break;
            case 4:
                this.palabra5 = p;
                break;
        }
        this.posicion++;

    }

    public ListaPalabrasIterador iterador()
    {
        return new ListaPalabrasIterador(this.palabra1, this.palabra2, this.palabra3, this.palabra4, this.palabra5);
    }
}
