/*

 */
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Moficiar a travez de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es:  = " + persona1.nombre); //error
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obetener el booleano: "+persona1.isEliminado());
        //Tarea Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1: "+persona1.toString());
        System.out.println("persona1 = " + persona1);
    }
}
