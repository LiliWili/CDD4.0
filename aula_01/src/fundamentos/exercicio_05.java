package fundamentos;
import java.util.Scanner;

public class exercicio_05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite a letra do seu genero: ");
        char letra = entrada.next().charAt(0);
        if (letra == 'F' || letra == 'f') {
            System.out.println("F de feminino");}
        else if (letra == 'M' ||letra =='m'){
            System.out.println("M de masculino");}
        else {
            System.out.println("Letra invalida");}
    }
}