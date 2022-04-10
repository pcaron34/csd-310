import java.util.Scanner;

import javax.swing.JOptionPane;

public class test{
    public static void main(String[] args) {
        int number1 = (int)(Math.random() * 10);
        int number2 = (int)(Math.random() * 10);

        Scanner input = new Scanner(System.in);

        System.out.print("What is " + number1 + " + " + number2 + "? ");
        int answer = input.nextInt();

        while (number1 + number2 != answer){
            System.out.print("Wrong answer. Try again. What is " + number1 + " + " + number2 + "? ");
            answer = input.nextInt();
        }
        System.out.println("You got it!");

        /********************************************************
         * Beginning
         */
        int i = 0;
        do{
            i = Integer.parseInt(JOptionPane.showInputDialog("Enter a positive interger to continue ..."));
            System.out.printf("The value entered is %d\n", i);
        }while(i > 0);
        System.out.println("The program has ended.");

         /********************************************************
          * end
          */
        
    }
}

