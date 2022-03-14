public class App {
    public static void main(String[] args) {
        BackEnd backend = new BackEnd();
        Middle middle = new Middle(backend);
        FrontEnd frontend = new FrontEnd(middle);
        
        frontend.getAyuda(2);
    }    
}
