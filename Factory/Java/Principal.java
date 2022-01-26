public class Principal {

    public static void main(String[] args){
        ShapeFactory shapeFactory = new ShapeFactory();

        // Construyendo un objeto de tipo triangulo
        Shape triangulo = shapeFactory.getShape("TRIANGLE");
        triangulo.draw(); // Dibujando el circulo

        System.out.println("");
        // Construyendo un objeto tipo rectangulo
        Shape rectangulo = shapeFactory.getShape("RECTANGLE");
        rectangulo.draw(); // dibujando el rectangulo

        System.out.println("");
        // Construyendo un objeto tipo cuadrado
        Shape cuadrado = shapeFactory.getShape("SQUARE");
        cuadrado.draw(); // dibujando el cuadrado


    }
    
}
