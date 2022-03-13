package Java;

import java.util.ArrayList;
import java.util.List;

public class Exodia implements Carta {
    private List<Carta> exodiaParts;

    Exodia()
    {

        exodiaParts = new ArrayList<>();
        
        exodiaParts.add(new Torso());
        exodiaParts.add(new PiernaDerecha());
        exodiaParts.add(new BrazoIzquierdo());
        exodiaParts.add(new PiernaIzquierda());
        exodiaParts.add(new BrazoDerecho());
 
    }

    @Override
    public void logic() {
        
        for(Carta pieza: exodiaParts){
            pieza.logic();
        }
        
    }
}