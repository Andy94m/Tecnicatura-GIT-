package holamundo;

import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.println ( "Hola mundo ");
        
        int miVariable = 10;
        System.out.println(miVariable);*/

        /*uso de VAR y sus tipos de datos
        var miVariableEntera2  = 10;
        var miVariableString2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableString2);
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
 
        //concatenacion
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;

        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(a + b);
        
        //contexto de cadena: analiza la primera variable y luego concatena
        System.out.println(usuario + a + b);
        
        
        //cambio de prioridad en la lectura
        System.out.println(usuario + (a + b));
        
        
        //salto de linea
        var nombre = "Natalia";
        System.out.println("Nueva linea : \n " + nombre);
        
        //tabulador
        System.out.println("Tabulador: \t " + nombre);
        
        //retrosede un espacio hacia atras
        System.out.println("Retroseso : \b " + nombre);
        
        //uso de comilla simple
        System.out.println("Comillas simples: \' " + nombre + " ' ");
        
        //uso de comillas dobles
        System.out.println("Comillas Dobles : \" " +nombre + " \" " ); 
        
        

        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado : " +titulo2+ " "+usuario2); 
        
        
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte " + Byte.MAX_VALUE);
        
        System.out.println("\n");
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short " + Short.MAX_VALUE);
        
        System.out.println("\n");
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int " + Integer.MAX_VALUE);
        
        System.out.println("\n");
        
        //Java por defecto asigna en INT asi que al final de una variable LONG cercano al maximo se coloca la "L"   
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long " + Long.MAX_VALUE); 
        
        System.out.println("\n");
        
        //Por deecto asigna en double y se debe colocar una "F" al final
        float numFloat = 3.4028235E38F; //tambien se usa numFloat = (float)10.0F
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo del float : " + Float.MIN_VALUE);
        System.out.println("El valor maximo del float : " + Float.MAX_VALUE);
        
        System.out.println("\n");
        
        
        //no hace falta ponerle "D" de double al final por que cualquier numero con coma lo interpreta como double por defecto
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de numDouble : " + Double.MIN_VALUE);
        System.out.println("El valor maximo de numDouble : " + Double.MAX_VALUE); 
        
        
        
        //inferencia de tipos var y tipos primitivos
        var numEntero = 20; //las literales sin punto por defecto son tipo INT
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //con el punto se transforma en double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble); 
        
        
        //tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        
        char varCaracter = '\u0024'; //asignacion con codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //valor decima de UNICODE
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //copiando caracter especiial de UNICODE
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        
        //comprobacion de inferencia de tipos
        var varCaracter2 = '\u0024'; 
        System.out.println("varCaracter2 = " + varCaracter2);
        var varCaracterDecimal2 = (char)36; //se castea o muestra un valor INT
        System.out.println("varCaracterDecimal2 = " + varCaracterDecimal2);
        var varCaracterSimbolo2 = '$'; 
        System.out.println("varCaracterSimbolo2 = " + varCaracterSimbolo2);
        
        
        //int soporta el valor decimal asociado al simbolo
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar); 
        
        
        
        //Tipos booleanos
        boolean varBool = true;
        System.out.println("VarBool = " + varBool);
        
        if (varBool){
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es roja");
        } 
        
        //Algoritmo: ¿Es mayor de edad?
        var edad = 20; //literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una expresion booleana
        if (edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else {
            System.out.println("Eres menor de edad");
        }  
        
        
        
        //Conversion de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //Pedir un valor 
        var entrada = new Scanner(System.in);
        //System.out.println("Digite su edad: ");
        //edad = Integer.parseInt (entrada.nextLine());
        //System.out.println("edad = " + edad); 
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
            
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(3);
        System.out.println("fraseChar = " + fraseChar); 
        
        int num1 = 5, num2 = 4; //no se puede asignar multiples variables con VAR
        var solucion = num1 + num2;
        System.out.println("Solucion suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("Solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("Solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("Solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("Resultado de la division flotante = " + solucion2);
        
        solucion = num1 % num2; //guarda residuo entero de la division
        System.out.println("solucion = " + solucion);
        
        
        if (num2 % 2 == 0)
            System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero Impar"); */
        
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; //una operacion
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //varNum1 = varNum1 + 1;
        
        System.out.println("varNum1 = " + varNum1);
        
        
    }
}
