public class Juego{
    private String nombre;
    private int checkPoint;

    public int getCheckPoint()
    {
        return this.checkPoint;
    }

    public void setCheckPoint(int checkPoint)
    {
        this.checkPoint = checkPoint;
    }

    public String getNombre()
    {
        return this.nombre; 
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    @Override
    public String toString()
    {
        return "Juego [nombre " + nombre + " checkpoint= " + checkPoint + "]";
    }
}