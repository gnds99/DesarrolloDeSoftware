public class Motor implements Observador {

    Motor(){}
    @Override
    public void update() {
        // esto sucede cuando se pisa el acelerador
        System.out.println("Subir la potencia");
        
    }
}
