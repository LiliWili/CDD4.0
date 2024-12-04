package fundamentos;

import java.util.Scanner;

public class exercicio_02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite o primeiro numero: ");
        double n1 = entrada.nextDouble();
        
        System.out.println("Digite o segundo numero: ");
        double n2 = entrada.nextDouble();
        
        System.out.println("Digite o terceiro numero: ");
        double n3 = entrada.nextDouble();
        
        if (n1 > n2 && n1 > n3) {
            System.out.println("O maior numero é " + n1);
        } else if (n2 > n3) {
            System.out.println("O maior numero é " + n2);
        } else {
            System.out.println("O maior numero é " + n3);
        }
    }
}
