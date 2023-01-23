# a simple review of if statements in Python

def main():
    x = 5
    y = 10
    z = 15

    if x > y:
        print("x is greater than y")
    elif y > x:
        print("x is less than y")
    else:
        print("x is equal to y")

    if x > y and x > z:
        print("x is the greatest")
    elif y > x and y > z:
        print("y is the greatest")
    elif z > x and z > y:
        print("z is the greatest")
    else:
        print("x, y, and z are equal")


if __name__ == "__main__":
    main()
