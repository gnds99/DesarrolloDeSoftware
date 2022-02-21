Patrones de diseño

Alumno: Gilberto Noe De la luz Seseña

Singleton

* Explicacion:
Singleton es usado cuando queremos crear una instancia de una clase en concreto, y limitar la creacion de instancias posteriores a lo largo del programa.

* Elementos:
  1.- Un constructor tipo private.
  2.- Un constructor tipo private que verifique si ya existe una instancia de su clase.
  
Java.
 

public class Main {
 public static void main(String[] args) 
 {
          Singleton miSingleton = Singleton.getSingleton();

          Singleton otroSingleton=Singleton.getSingleton();

          System.out.println(miSingleton==otroSingleton);
    }
}

public class Singleton 
{
    static private Singleton singleton = null;
    private Singleton(){}
    static public Singleton getSingleton(){
       if (singleton == null){
           singleton = new Singleton();
       }
       return singleton;
    }
}

-> Python
--------------

--------------

* Caso de uso:
  1.- Crear una conexion para una base de datos

+-------------------------------------------------------------------------------------------------------------------+

Builder:

* Explicacion:

  Es un patron de diseño creacional que permite construir objetos complejos paso a paso. Este patron permite la creacion (producción) de diferentes tipos
  y representaciones de un objeto usando el mismo código de construcción.

* Elementos:
  1.- Clases concretas
  2.- Clase abstracta
  3.- Clases concretas que heredan las abstractas
  4.- Clase creacional
  5.- Clase cliente
 
 -> Java
 
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

public class HawaiPizzaBuilder extends PizzaBuilder
{

    @Override
    public void buildMasa()
    {
        pizza.setMasa("suave");
    }
      
    @Override 
    public void buildSalsa()
    {
        pizza.setSalsa("dulce");
    }
    
    @Override
    public void buildRelleno()
    {
        pizza.setRelleno("peperoni");
    }
}

public abstract class PizzaBuilder {

    protected Pizza pizza;
    public Pizza getPizza()
    {
        return pizza;
    }
    public void crearNuevaPizza()
    {
        pizza = new Pizza();
    }
    public abstract void buildMasa();
    public abstract void buildSalsa();
    public abstract void buildRelleno();
    
}

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

--------------

-> Python
--------------

--------------

* Caso de uso:
  1.- En un videojuego, cuando se quieren crear diferentes tipos de autos con caracteristicas diferetes
  

+-------------------------------------------------------------------------------------------------------------------+

Factory

* Explicación:

  En el patron de diseño Factory, creamos un objeto sin exponer la lógica de creacion al cliente y nos referimos a un objeto recien creado usando 
  una interfaz comun. 

  El patron factory es el encargado de crear diferentes tipos de objetos de multiples clases pero con caracteristicas diferentes o de una misma pero
  de igual manera con diferentes caracteristicas.
  
* Elementos:

 1.- Una interfaz o clase abstracta
 2.- Clases concretas
 3.- Una clase factory que retorna un obejto de una clase concreta que hereda de la abstracta
 4.- Clase principal de ejecucion (cliente)

 
 -> Java
  
public interface Shape{
    void draw();
}

public class Rectangle implements Shape {

    @Override
    public void draw()
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                System.out.print("* ");
            }
            System.out.println("");
        }
    }
    
}


public class Square implements Shape {

    @Override
    public void draw()
    {
        for(int i = 0; i < 5; i++)
        {
            for(int j = 0; j < 5; j++)
            {
                System.out.print("* ");
            }
            System.out.println(" ");
        }
    }
    
}

public class ShapeFactory {

    //use getShape method to get object of type shape 
    public Shape getShape(String shapeType){
       if(shapeType == null){
          return null;
       }		
       if(shapeType.equalsIgnoreCase("TRIANGLE")){
          return new Triangle();
       } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
          return new Rectangle();
       } else if(shapeType.equalsIgnoreCase("SQUARE")){
          return new Square();
       }
       return null;
    }
 }
 
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
--------------

-> Python
class shape(object):

    numLados = 0
    def __init__(self, numLados):
        print("figura construida")
        self.numLado = numLados
    def draw(self):
        print("Imprimiendo figura")
    def getLados(self):
        print(self.numLados)
   
from Shape import shape

class square(shape):

    """ Esta clase hereda de la super clase Shape """
    def __init__(self, numLados):
        print("Cuadrado")
        self.numLados = numLados
    def draw(self):
        for i in range(0, self.numLados):
            for j in range(0, self.numLados):
                print("* ", end="")
            print(" ")    
            
from Shape import shape
 
class rectangle(shape):

    """ Esta clase hereda de la super clase Shape """
    def __init__(self, numLados):
        print("Rectangulo")
        self.numLados = numLados
    def draw(self):
        for i in range(0, self.numLados):
            for j in range(0, self.numLados*2):
                print("* ", end="")
            print(" ")

from Rectangle import rectangle

from Square import square

class shapeFactory(object):
  
    def get_Shape(self, figura, numlados):
        if(figura == 'r'):
            return rectangle(numlados)
        elif(figura == 's'):
            return square(numlados)

import ShapeFactory

if __name__ == '__main__':
    mi_shape = ShapeFactory.shapeFactory()
    rectangulo = mi_shape.get_Shape('r', 4)
    rectangulo.getLados()
    rectangulo.draw()
    cuadrado = mi_shape.get_Shape('s', 2)   
    cuadrado.getLados()
    cuadrado.draw()
    
--------------

Caso de uso: Podemos poner de ejemplo nuevamente un videojuego que requiero que se genere de manera aleatoria los enemigos para soprender a los jugadores
evitando relacionar un enemigo a cada mapa o nivel. Asi como tambien para crear variaciones de un solo enemigo, volviendolo mas fuerte o debil por ejemplo.

+-------------------------------------------------------------------------------------------------------------------+

Prototype

* Explicacion:

  Es un patron de diseño creacional que permite copiar objetos existentes sin hacer que su codigo dependa de sus clases o para modificar un cierto tipo
  de objeto conservando el original.

* Elementos:
  1.- Se requiere de una interfaz o clase obstracta con un metodo de clone() este es opcional ya que puedes usar el que viene integrado con java
  2.- Clases concretas
  3.- Clase principal

-> Java
--------------
public interface Figura {

    public void setNombre(String n);
    public String getNombre();
    public void mover(int x, int y);
    public void getPosicion();
    public Figura clonar();
}
public class Circulo implements Figura {

    private String nombre;
    private int posicionX, posicionY;
    public Circulo(String nombre, int x, int y){this.nombre = nombre; this.posicionX = x; this.posicionY = y;}
    public Circulo(){}
    @Override
    public void setNombre(String n){
        this.nombre = n;
    }
    @Override
    public String getNombre(){
        return nombre;
    }
    @Override
    public void mover(int x, int y)
    {
        this.posicionX = x;
        this.posicionY = y;
    }
    @Override
    public void getPosicion(){
        System.out.println("Circulo en x: " + this.posicionX);
        System.out.println("Circulo en y: " + this.posicionY);
    }
    @Override
    public Figura clonar(){
        Figura figura = new Circulo();
        figura.setNombre(this.nombre);
        figura.mover(this.posicionX, this.posicionY);
        return figura;
    }
}
  
public class Cuadrado implements Figura {

    private String nombre;
    private int posicionX, posicionY;
    public Cuadrado(String nombre, int x, int y){this.nombre = nombre; this.posicionX = x; this.posicionY = y;}
    //public Circulo(){}
    @Override
    public void setNombre(String n){
        this.nombre = n;
    }
    @Override
    public String getNombre(){
        return nombre;
    }
    @Override
    public void mover(int x, int y)
    {
        this.posicionX = x;
        this.posicionY = y;
    }
    @Override
    public void getPosicion(){
        System.out.println("Cuadrado en x: " + this.posicionX);
        System.out.println("Cuadrado en y: " + this.posicionY);
    }
    @Override
    public Figura clonar(){
        Figura figura = new Circulo();
        figura.setNombre(this.nombre);
        figura.mover(this.posicionX, this.posicionY);
        return figura;
    }
}

public class Principal {

    public static void main(String [] args)
    {
        Circulo circulo = new Circulo("Mi circulo", 10, 10);
        Cuadrado cuadrado = new Cuadrado("Mi rectanuglo", 15, 15);
        System.out.println("Informacion del circulo");
        System.out.println(circulo.getNombre());
        circulo.getPosicion();
        System.out.println("Informacion del cuadrado");
        System.out.println(cuadrado.getNombre());
        cuadrado.getPosicion();
        // clonando 
        Figura figura;
        figura = circulo.clonar();
        figura.setNombre("Figura clon del circulo");
        System.out.println(figura.getNombre());
        figura.mover(10,-10);
        figura.getPosicion();;
    }
    
}
--------------

-> Python:

--------------


--------------

* Caso de uso:
  Crear un elemento prefabricado como se hace en unity. Se crea un objeto y posteriomente se va clonando y se le realizan modificaciones sobre la marcha
  



  


