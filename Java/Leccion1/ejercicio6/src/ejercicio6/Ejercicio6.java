
package ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main (String[] args){
        Scanner entrada = new Scanner (System.in);
        float guillermo, luis, juan, total;
        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("\n El dinero de Luis es : US$ " + luis);
        System.out.println("El dinero de Juan es : US$ " + luis);
        System.out.println("El total del dinero entre los tres es: US$ " + total);
    }   
}



