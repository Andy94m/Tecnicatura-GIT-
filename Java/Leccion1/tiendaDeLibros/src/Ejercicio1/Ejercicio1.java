
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 { 
    public static void main(String[] args) {
        Scanner ingreso = new Scanner (System.in);
         System.out.println("\t INGRESE LOS SIGUIENTES DATOS DEL LIBRO: \n");
         //INGRESO DE DATOS DEL LIBRO
         System.out.println("Digite el nombre del libro: ");
         String nombreDelLibro = ingreso.nextLine();
         System.out.println("Digite el ID del libro: ");
         int idDelLibro = Integer.parseInt(ingreso.nextLine());
         System.out.println("Digite el precio del libro: ");
         float precioDelLibro = Float.parseFloat(ingreso.nextLine());
         System.out.println("¿El envi­o es gratuito? (true/false): ");
         boolean envioDelLibro = Boolean.parseBoolean(ingreso.nextLine());
                 
         System.out.println("\n");
         
         //MUESTRA DE DATOS     
         System.out.println("\t LOS DATOS DEL LIBRO SON: \n");
         System.out.println("Nombre del libro = " + nombreDelLibro);
         System.out.println("ID = " + idDelLibro);
         System.out.println("Precio = $ " + precioDelLibro);
         System.out.println("El envi­o es = " + envioDelLibro);
    }
    
}

