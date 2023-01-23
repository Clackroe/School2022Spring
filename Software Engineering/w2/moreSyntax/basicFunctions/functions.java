// a simple review to show how functions work in Java
package w2.moreSyntax.basicFunctions;

public class functions {

    // function definition
    public static void greeting(String name) {
        // function body
        System.out.println("Hello, " + name);
    }

    public static int add(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {
        // calling the function
        greeting("John");
        greeting("olleH");

        // calling the add function and storing the result in a variable
        int result = add(1, 2);
        System.out.println(result);
    }
}
