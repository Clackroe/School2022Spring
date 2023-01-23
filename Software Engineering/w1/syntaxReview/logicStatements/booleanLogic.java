// simple boolean logic in Java
package w1.syntaxReview.logicStatements;

public class booleanLogic {
    public static void main(String[] args) {
        boolean x = true;
        boolean y = false;
        if (x && y) {
            System.out.println("x and y are true");
        } else if (x || y) {
            System.out.println("x or y is true");
        } else {
            System.out.println("x and y are false");
        }

    }

}
