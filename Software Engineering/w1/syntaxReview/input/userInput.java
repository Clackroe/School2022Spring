// getting user input in Java
package w1.syntaxReview.input;

import java.util.Scanner;

public class userInput {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scnr.nextLine();
        System.out.println("Hello, " + name);
        scnr.close();
    }
}