package fundamentos2;
//Descobrir os numeros  impares de 0 a 50

public class exercicio_03 {
	public static void main(String[] args) {
 
		for(int numero=1; numero<=50; numero++) {
			if (numero %2!=0) {
				System.out.println("Estes numeros são pares: " + numero);
			}
		}
	}
}
 