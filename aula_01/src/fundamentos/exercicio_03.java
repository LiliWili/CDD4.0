package fundamentos;

import java.util.Scanner;

public class exercicio_03 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
        System.out.println("Digite o primeiro numero: ");
        int n1 = entrada.nextInt();
        
        if (n1 == 1) {
        	System.out.println("O dia da semana é domingo");}
        	else if (n1 == 2) {
        		System.out.println("O dia da semana é segunda");}
        	else if(n1==3) {
        		System.out.println("O dia da semana é terça");}
        	else if(n1==4) {
        		System.out.println("O dia da semana é quarta");}
        	else if(n1==5) {
        		System.out.println("O dia da semana é quinta");}
        	else if(n1==6) {
        		System.out.println("O dia da semana é sexta");}
        	else if(n1==7) {
        		System.out.println("O dia da semana é sabado");}
        	else{
        		System.out.println("O valor é invalido");}
        
        switch (n1){
        case 1:
        	System.out.println("O dia da semana é domingo");
        	break;
        case 2:
        	System.out.println("O dia da semana é segunda");
        	break;
        case 3:
        	System.out.println("O dia da semana é terça");
        	break;
        case 4:
        	System.out.println("O dia da semana é quarta");
        	break;
        case 5:
        	System.out.println("O dia da semana é quinta");
        	break;
        case 6:
        	System.out.println("O dia da semana é sexta");
        	break;
        case 7:
        	System.out.println("O dia da semana é sabado");
        	break;
        default:
        	System.out.println("numero invalido");
        	break;
  
      }       
   }     
}
