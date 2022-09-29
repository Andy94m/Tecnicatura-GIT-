package clase11ej1;

import java.util.Scanner;

public class Clase11Ej1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        
        int nota1, nota2, nota3, promedio;
        
        System.out.println("Digite las 3 calificaciónes a promediar: ");
        nota1 = Integer.parseInt(entrada.nextLine());
        nota2 = Integer.parseInt(entrada.nextLine());
        nota3 = Integer.parseInt(entrada.nextLine());
        
        promedio = (nota1 + nota2 + nota3) / 3;
        
        //System.out.println("\nSu promedio es: " + promedio);
        
        if (promedio >= 7){
            System.out.println("El alumno esta aprobado y su promedio es: " + promedio);   
        }
        else{
            System.out.println("El alumno esta desaprobado y su promedio es: " + promedio);
        }
    }
    
}
