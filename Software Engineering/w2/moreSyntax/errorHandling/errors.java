// a simple example of error handling in Java
package w2.moreSyntax.errorHandling;

public class errors {

    public static void basicException(String[] args) {
        try {
            int[] myNumbers = { 1, 2, 3 };
            System.out.println(myNumbers[10]);
        } catch (Exception e) {
            System.out.println("Something went wrong...");
        }
    }

    public static void numberFormatException(String[] args) {
        try {
            int x = Integer.parseInt("abc");
            x = x + 1;

        } catch (NumberFormatException e) {
            System.out.println("Number format exception");
        }
    }
}
