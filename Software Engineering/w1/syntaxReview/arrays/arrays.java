package w1.syntaxReview.arrays;

public class arrays {
    public static void main(String[] args) {
        int[] myArray = new int[10];
        for (int i = 0; i < 5; i++) {
            myArray[i] = i + 1;
        }
        for (int i = 0; i < 10; i++) {
            // add a value to the array if i > 4
            if (i > 4) {
                myArray[i] = i + 1;
            }
            System.out.println("myArray at index " + i + " = " + myArray[i]);
        }
    }
}