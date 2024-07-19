import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int nowMaxNumber = 0;
        int nowMaxIndex = 0;
        for (int i=0; i<9; i++){
            int number = sc.nextInt();
            if (number > nowMaxNumber){
                nowMaxNumber = number;
                nowMaxIndex = i+1;
            }
        }
        System.out.println(nowMaxNumber);
        System.out.println(nowMaxIndex);
    }
}