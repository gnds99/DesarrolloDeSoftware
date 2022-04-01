public class App 
{
    public static void main(String args[])
    {
        Motor v8 = new Motor();
        Acelerador x = new Acelerador();    
    
        x.attach(v8);
        x.pisarAcelerador();
    }
}
