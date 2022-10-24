
package cliclowhile;

public class ClicloWhile {  
    public static void main(String[] args) {
        var conteo = 0; //inferenciia de tipos
        while (conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        
        //inicio:
        for(var contando = 0; contando < 7; contando ++ ){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        }
        
        
        inicio:
        for(var contando = 0; contando < 7; contando ++ ){
            if(contando % 2 != 0){
                continue inicio; //continua con la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }

        //Etiquetas Labels, go to
 
    }
    
}
