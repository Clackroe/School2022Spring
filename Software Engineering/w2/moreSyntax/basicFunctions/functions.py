# a simple review to show how functions work in Python

# function definition
def greeting(name):
    # function body (MUST BE INDENTED ONE TAB)
    print(f"Hello, {name}")


def add(x: int, y: int) -> int:
    """
    Optionally, we can use type hints to specify parameter and return types.
    This is not required, but it is good practice.
    Python will not enforce these types.
    """
    return x + y


def main():
    # calling the function
    greeting("John")
    greeting("olleH")

    # calling the add function and storing its return value
    num_sum = add(1, 2)
    print(num_sum)

    # calling the add function on two strings and immediately printing the result
    print(add("Hello, ", "World!"))


if __name__ == "__main__":
    main()
