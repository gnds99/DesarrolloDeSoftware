public class Principal {
    public static void main(String[] args)
    {
        Cocina cocina = new Cocina();
        PizzaBuilder hawai = new HawaiPizzaBuilder();

        cocina.setPizzaBuilder(hawai);
        cocina.construirPizza();

        Pizza pizza = cocina.getPizza();
        pizza.dataPizza();
    }
}
