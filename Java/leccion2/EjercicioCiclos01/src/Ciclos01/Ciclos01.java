/*ejercico 1: leer un numero y mostrar su cuadrado
, repetir el proceso hasta que se introduzca un numero negrativo */

package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero " +numero+ "ELEVADO AL CUADRADO ES: "+ cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa fiinalizó");
    }
    
}
