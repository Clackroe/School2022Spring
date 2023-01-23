// a simple review to show how classes work in Java
package w2.moreSyntax.basicClasses;

public class basicClass {

    // class definition
    static class Person {
        // class body
        String name;
        int age;

        // constructor
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        // method definition
        public void greeting() {
            System.out.println("Hello, my name is " + name);
        }

        public void sayAge() {
            System.out.println("I am " + age + " years old");
        }
    }

    public static void main(String[] args) {
        // creating an instance of the class (an object)
        Person person1 = new Person("George", 20);
        Person person2 = new Person("Georgia", 21);

        // calling the methods
        person1.greeting();
        person1.sayAge();
        person2.greeting();
        person2.sayAge();

    }
}