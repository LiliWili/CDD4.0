package fundamentos2;
import java.util.Scanner;

public class exercicio_01 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int qtd_alunos = 0, cont =0;
		float notas =0;
		System.out.println("Digite a quantidade de alunos: ");
		qtd_alunos = entrada.nextInt();
		
		while(cont < qtd_alunos) {
			System.out.println("Digite as notas dos alunos: ");
			notas += entrada.nextFloat();	
			cont++;
		}
		float resultado = notas/qtd_alunos;
		System.out.println("Esta é a media da sala "+ resultado);
	}
}
