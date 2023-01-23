# simple boolean logic in Python

def main():
    x, y = True, False  # python allows multiple assignment on one line

    if x and y:
        print("x and y are true")
    elif x or y:
        print("x or y is true")
    else:
        print("x and y are false")


if __name__ == "__main__":
    main()
