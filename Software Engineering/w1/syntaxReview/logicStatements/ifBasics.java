// a simple review of if statements in Java
package w1.syntaxReview.logicStatements;

public class ifBasics {
    public static void main(String[] args) {
        int x = 5;
        int y = 10;
        int z = 15;

        if (x > y) {
            System.out.println("x is greater than y");
        } else if (x < y) {
            System.out.println("x is less than y");
        } else {
            System.out.println("x is equal to y");
        }

        if (x > y && x > z) {
            System.out.println("x is the greatest");
        } else if (y > x && y > z) {
            System.out.println("y is the greatest");
        } else if (z > x && z > y) {
            System.out.println("z is the greatest");
        } else {
            System.out.println("x, y, and z are equal");
        }
    }

}
