public class FrontEnd implements InterfaceAyuda {

    private final int TIPO_AYUDA = 1;
    private InterfaceAyuda sucesor;
   
   FrontEnd(InterfaceAyuda s)
   {
       this.sucesor = s;
   }

    @Override
    public void getAyuda(int tipo) {
        if(tipo == TIPO_AYUDA){
            System.out.println("Ayuda desde el frontEnd");
        } else{
            sucesor.getAyuda(tipo);
        }
    }
    
}
