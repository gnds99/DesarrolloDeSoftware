public class Pizza {

    private String masa = "";
    private String relleno = "";
    private String salsa = "";


    public void setMasa(String masa)
    {
        this.masa = masa;
    }

    public void setRelleno(String relleno)
    {
        this.relleno = relleno;
    }

    public void setSalsa(String salsa)
    {
        this.salsa = salsa;
    }
    
    public void dataPizza()
    {
        System.out.println("");
        System.out.print("Pizza Hawaiana\n\n" + "Tipo masa: " + this.masa + "\nTipo Salsa: " + this.salsa + "\nTipo de relleno: " + this.relleno);
    }
}
