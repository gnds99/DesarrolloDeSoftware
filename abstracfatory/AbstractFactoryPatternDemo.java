public class AbstractFactoryPatternDemo {

    public static void main(String[] args){

        // obteniendo shape factory
        AbstractFactory shapeFactory = FactoryProducer.getFactory(false);
        // obteniendo un objeto de en forma de rectangulo
        Shape shape1 = shapeFactory.getShape("RECTANGLE");
        // Llamando el metodo  dibujo del rectangulo
        shape1.draw();
        // obteniendo un objeto en forma de cuadrado
        Shape shape2 = shapeFactory.getShape("SQUARE");
        //Llamando el motod dibujo del cuadrado
        shape2.draw();

        AbstractFactory shapeFactory1 = FactoryProducer.getFactory(true);
        //obteneidno un obejto en forma de rectangulo
        Shape shape3 = shapeFactory1.getShape("RECTANGLE");
        //Llamando el metodo de dibujo del rectangulo
        shape3.draw();
        // obteniendo un objeto de la figura cuadrado
        Shape shape4 = shapeFactory1.getShape("SQUARE");
        //Llamando el metodo de dibujo del cuadrado
        shape4.draw();
    }
    
}
