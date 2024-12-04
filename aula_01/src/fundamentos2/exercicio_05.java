package fundamentos2;

import java.util.Scanner;

public class exercicio_05 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int qtd_alunos = 0;
		System.out.println("Digite a quantidade de alunos: ");
		qtd_alunos = entrada.nextInt();
		double notas=0, media =0;
		
		for(int x=0; x< qtd_alunos ; x++) {
			System.out.println("Digite as notas dos alunos: ");
			notas+= entrada.nextDouble();
		}
		media = notas/qtd_alunos;
		System.out.println("Esta é a media da sala "+ media);
		
	}
}
