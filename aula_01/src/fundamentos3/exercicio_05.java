package fundamentos3;

import java.util.Scanner;

public class exercicio_05 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um texto: ");
		String str = entrada.next();
		String resultado = str.toUpperCase();
		System.out.println(resultado);
	}

}
