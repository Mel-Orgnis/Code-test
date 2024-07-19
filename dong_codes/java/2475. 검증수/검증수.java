import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int sumOfSquareNumber = 0;
        for (int i=0; i<5; i++){
            int number = sc.nextInt();
            sumOfSquareNumber += number*number;
        }
        System.out.println(sumOfSquareNumber%10);
        
    }
}