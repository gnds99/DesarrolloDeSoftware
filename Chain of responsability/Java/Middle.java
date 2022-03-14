public class Middle implements InterfaceAyuda {
    
    private final int TIPO_AYUDA = 2;
    private InterfaceAyuda sucesor;

    Middle(InterfaceAyuda s)
    {
        this.sucesor = s;
    }
    @Override
    public void getAyuda(int tipo)
    {
        if(tipo == TIPO_AYUDA)
        {
            System.out.println("Ayuda desde el Middle");
        }else{
            this.sucesor.getAyuda(tipo);
        }
    }
}
