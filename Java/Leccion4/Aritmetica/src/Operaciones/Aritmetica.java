/*

 */
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un metodo especial
    public Aritmetica(){ //constructor vacio
        System.out.println("Se esta ejecutando este constructor nro uno");
    }
    
    //Viendo sobrecarga de constructores
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        int resultado = a + b;
        //return a + b; tambien se puede hacer así
        return resultado;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; //El argumento a se asigna al atributo this.a
        this.b = arg2;
        //return a + b;
        return sumarConRetorno();
    }
}
