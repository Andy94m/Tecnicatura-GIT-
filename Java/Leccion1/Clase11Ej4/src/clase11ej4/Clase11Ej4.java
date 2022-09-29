package clase11ej4;

import java.util.Scanner;

public class Clase11Ej4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        
        int num1, num2, resultado=0;
        
        System.out.println("Digite dos números: ");
        num1 = Integer.parseInt(entrada.nextLine());
        num2 = Integer.parseInt(entrada.nextLine());
        
        if (num1 == num2){
            resultado = num1 * num2;
        }
        else{
            if (num1 > num2){
                resultado = num1 - num2;
            }
            else{
                resultado = num1 + num2;
            }
        }
        
        System.out.println("El resultado es: " + resultado);
    }
    
}
