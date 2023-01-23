# a simple review to show how classes work in Python

# class definition
class Person:
    # class body (MUST BE INDENTED ONE TAB)

    # class constructor
    def __init__(self, name: str, age: int):
        # instance variables (attributes)
        self.name = name
        self.age = age

    # method definition (must pass self as first parameter)
    def greeting(self):
        print(f"Hello, my name is {self.name}")

    # another method definition
    def sayAge(self):
        print(f"I am {self.age} years old")


def main():
    # creating an instance of the Person class
    p1 = Person("George", 20)
    p2 = Person("Georgia", 21)

    # calling p1's methods
    p1.greeting()
    p1.sayAge()

    # NOTE: we do not need to pass self as a parameter when calling methods, only when defining them

    # calling p2's methods
    p2.greeting()
    p2.sayAge()


if __name__ == "__main__":
    main()
