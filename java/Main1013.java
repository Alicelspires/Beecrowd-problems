import java.util.Scanner;

public class Main1013{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        int maior = Math.max(a,Math.max(b, c));
        
        System.out.println(maior + " eh o maior");
    }
}