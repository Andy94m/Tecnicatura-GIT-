/*

 */
package caja;


public class Caja {  //clase publica caja
    //atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    
    //metodos y constructores (acciones)
    public Caja(){ //constructor 1 = vacio    
    }
    
    //Constructor con parametros    
    public Caja ( int ancho, int alto, int profundo) {//contructor2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //metodo para calcular
        return ancho * alto * profundo;
    }
}
