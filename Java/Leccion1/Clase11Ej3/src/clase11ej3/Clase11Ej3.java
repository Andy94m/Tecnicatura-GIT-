package clase11ej3;

import java.util.Scanner;

public class Clase11Ej3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        
        int compra;
        float descuento=0, precio_final=0;
        
        System.out.println("Digite la cantidad a pagar: ");
        compra = Integer.parseInt(entrada.nextLine());
        
        if (compra > 100){
            descuento = (compra * 20) / 100;
        }
        else{
            descuento = 0;
        }
        
        precio_final = compra - descuento;
        
        System.out.println("Su precio final es: " + precio_final);
    }
    
}
