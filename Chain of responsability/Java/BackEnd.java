public class BackEnd implements InterfaceAyuda {
    
    private final int TIPO_AYUDA = 3;

    BackEnd(){}

    @Override
    public void getAyuda(int tipoAyuda) {
        System.out.println("Ayuda desde el backEnd");        
    }

}
