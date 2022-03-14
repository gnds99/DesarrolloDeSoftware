import java.util.ArrayList;
import java.util.List;
public class Acelerador implements SujetoObservable
{
    private List<Observador> observers;
    

    Acelerador()
    {
        this.observers =  new ArrayList<Observador>();
    }

    public void pisarAcelerador()
    {
        // Vamos a subir la potencia del motor
        this.notificar();
    }

    public void attach(Observador o)
    {
        this.observers.add(o);
    }

    @Override
    public void notificar()
    {
        for(Observador o: observers){
            o.update();
        }
    }
}
