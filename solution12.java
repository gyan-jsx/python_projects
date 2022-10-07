import java.util.*;


public class solution12 {
    public static void main(String args[]) {
        Scanner scnr = new Scanner(System.in);
        double num1, num2, sumOfSquares;
        double inp1, inp2, inp3, maxNum;
        int number, remainder, reverse = 0, temp;
        int choice;
        
        System.out.println("Enter your choice: ");
        System.out.println("Applicable menu numbers are 1, 2, 3");
        choice = scnr.nextInt();
        switch(choice){
            case 1:
             System.out.println("Enter 1st number: ");
             num1 = scnr.nextDouble();
             System.out.println("Enter 2nd number: ");
             num2 = scnr.nextDouble();
             if(num1 > 20 && num2 > 20) {
                System.out.println("Before Swapping: " + num1 + " : " + num2);
                num1 += num2;
                num2 = num1 - num2;
                num1 = num1 - num2;
                System.out.println("Before Swapping: " + num1 + " : " + num2);
             }
             else {
                sumOfSquares = (Math.pow(num1, 2) + Math.pow(num2, 2));
                System.out.println("Sum of squares = " + sumOfSquares);
             }
             break;
             case 2:
              System.out.println("Enter the first number");
              inp1 = scnr.nextDouble();
              System.out.println("Enter the second number");
              inp2 = scnr.nextDouble();
              System.out.println("Enter the third number");
              inp3 = scnr.nextDouble();
              
              if(inp1 >= inp2 && inp1 >= inp3) {
                 System.out.println(inp1 + " is maximum");
              }
              else if(inp2 >= inp1 && inp2 >= inp3) {
                System.out.println(inp2 + " is maximum");
             }
             else if(inp3 >= inp2 && inp3 >= inp1) {
                System.out.println(inp3 + " is maximum");
             }

            if(inp1 <= inp2 && inp1 <= inp3) {
                System.out.println(inp1 + " is minimum");
            }
            else if(inp2 <= inp1 && inp2 <= inp1) {
                System.out.println(inp1 + " is minimum");
            }
            else if(inp3 <= inp2 && inp3 <= inp1) {
                System.out.println(inp1 + " is minimum");
            }
            break;
            case 3:
             System.out.println("Enter a number");
             number = scnr.nextInt();

             temp = number;
             while (number != 0) {
                remainder = number   % 10;
                reverse = reverse * 10 + remainder;
                number /= 10;
              }
              if (temp == reverse) {
                System.out.println(temp + " is Palindrome.");
              }
              else {
                System.out.println(temp + " is not Palindrome.");
              }
        }
    }
}










