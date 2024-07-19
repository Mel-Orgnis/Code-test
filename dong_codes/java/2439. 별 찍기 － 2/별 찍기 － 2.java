import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=1; i<=n; i++){
            leftWhite(i,n);
            rightStars(i);
            if(i!=n){
                System.out.println();
            }
        }

    }
    public static void rightStars(int idx){
        for (int i=0; i<idx; i++){
            System.out.print("*");
        }
    }
    public static void leftWhite(int idx, int n){
        for (int i=0; i < n - idx ; i++){
            System.out.print(" ");
        }
    }
}