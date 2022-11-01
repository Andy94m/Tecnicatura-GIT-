/*

 */
package caja;


public class PruebaCaja {
    public static void main(String[] args) { //metodo main
        //variables locales
        int medidaAncho = 3; //valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //pasamos valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al metodo
        
        //primer resultado
        System.out.println("Resultado volumen de caja 1: "+resultado);
        
        Caja caja2 = new Caja (2, 4, 6); //Llamamos al constructor 2 con nuevos argumentos
        //llamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("Resultado volumen de caja2: "+caja2.calcularVolumen());
    }
}
