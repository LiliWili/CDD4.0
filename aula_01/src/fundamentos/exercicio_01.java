package fundamentos;

import java.util.Scanner;

public class exercicio_01 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		double resp = entrada.nextDouble();
		if (resp > 0) {
			System.out.println("O numero é positivo" + resp);
		}
		else {
			System.out.println("O numero é negativo" + resp);
		}		
	}
}
