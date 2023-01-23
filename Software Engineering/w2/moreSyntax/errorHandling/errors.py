# a simple example of error handling in Python

def basicError():
    try:
        myNumbers = [1, 2, 3]
    except Exception:
        # Exception is the base class for all errors
        print("Something went wrong")


def indexError():
    try:
        myNumbers = [1, 2, 3]
    except IndexError:
        # IndexError is raised when an index is out of range
        print("Index out of range")


def valueError():
    try:
        myNumbers = [1, 2, 3]
    except ValueError as e:
        # ValueError is raised when a value is not of the expected type
        print("Value error: ", e)


def main():
    basicError()
    indexError()
    valueError()


if __name__ == "__main__":
    main()
