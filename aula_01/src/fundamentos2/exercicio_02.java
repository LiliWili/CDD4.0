package fundamentos2;
//Descobrir os numeros  impares de 0 a 50

public class exercicio_02 {
	public static void main(String[] args) {
		int numero = 0;
		while(numero < 50) {
			if (numero %2!=0) {
				System.out.println("Estes numeros são pares: " + numero);
			}
			numero++;
		}
	}
}
