package fundamentos3;

public class exemplo_07 {
	public static void main(String[] args) {
		String s1 = "Hello";
		String s2 = "HELLO";
		boolean b1 = s1.equals ("Hello");
		boolean b2 = s1.equals(s2);
		boolean b3= s1.equalsIgnoreCase(s2);
		boolean b4 = s1.equalsIgnoreCase("azul");
		
		if(b1 == true) {
			System.out.println("São iguais");}
		else {
			System.out.println("Não são iguais");}
		if(b2 == true) {
			System.out.println("São iguais");}
		else {
			System.out.println("Não são iguais");}
		if(b3 == true) {
			System.out.println("São iguais");}
		else {
			System.out.println("Não são iguais");}
		if(b4 == true) {
			System.out.println("São iguais");}
		else {
			System.out.println("Não são iguais");}
	}
}