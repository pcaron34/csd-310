import javax.swing.*;

public class Test2{
    public static void main(String[] args){
        int i = 0;

        do{
            i = Integer.parseInt(JOptionPane.showInputDialog("Enter a positive interger to continue ..."));
            System.out.printf("The value entered is %d\n", i);

        }while(i > 0);
        System.out.println("This program has ended.");
    }
}



public class loopingProgram{
    public static void main(String[] args){
        
        int a = 1;
         
        while(a < 99){
            a = a + 2;
            System.out.print("1/" + a + " " + "+" + " ");
                        
        }
    }

   
}

int a = 1;
         
        while(a < 99){
            a = a + 2;
            
            System.out.print("1/" + a + " " + "+" + " ");
            a = a.replaceAll("+", "")