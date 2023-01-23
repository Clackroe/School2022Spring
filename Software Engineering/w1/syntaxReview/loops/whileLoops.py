# basic while loops in Python

def main():
    x = 0

    while x < 10:
        # f-strings allow for easy string formatting
        print(f"Looping: x is {x}")
        x *= 2  # this is the same as x = x * 2

    print(f"x is now {x}")


if __name__ == "__main__":
    main()
