/*

 */
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10; //Variables locales
        int b = 7; //Memoria stack
        miMetodo(); //llamamos el nuevo metodo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        //aritmetica1 = null;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto o los atributos se utiliza memoria Heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = "+aritmetica2.a);
        System.out.println("aritmetica2 = "+aritmetica2.b);
        //aritmetica1 = null; //no utilizar el null
        //System.gc(); //garbage colector, limpia pero es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("Persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona nombre: " + persona.apellido);
    }
    
    //modularidad creamos un nuevo metodo
    public static void miMetodo(){
        //a = 10; //Una variable limitada
        System.out.println("Aqui hay otro metodo");
    }
}

class Persona{
    String nombre;
    String apellido;
    
    Persona (String nombre, String apellido){ //Constructor
        super(); //LLamada al constructor de la clase Padre object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir = " +persona);
        System.out.println("impresion del objeto actual (this) = " +this);
    }
}
