package fundamentos;

import java.util.Scanner;

public class exercicio_06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite 1 para sim 0 para não");
        
        System.out.println("Telefonou para a vitima? ");
        int numero = entrada.nextInt();
        System.out.println("Esteve no local do crime? ");
        numero += entrada.nextInt();
        System.out.println("Mora perto da vitima? ");
        numero += entrada.nextInt();
        System.out.println("Devia para a vitima? ");
        numero += entrada.nextInt();
        System.out.println("Ja trabalhou com a vitima? ");
        numero += entrada.nextInt();
        
        if (numero == 5){
        	System.out.println("Você é culpado");}
        else if(numero >=3 && numero <=4) {
        	System.out.println("Voce é cumplice");}
        else if(numero == 2) {
        	System.out.println("Voce é suspeito");}
        else {
        	System.out.println("Voce é inocente");
        }
    }
}