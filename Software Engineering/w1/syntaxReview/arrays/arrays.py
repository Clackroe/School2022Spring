# a basic review of arrays (lists) in Python

def main():
    # arrays have no initial size in python
    # we can declare values immediately
    myArray = [1, 2, 3, 4, 5]
    for i in range(10):
        print(f"myArray at index {i} = {myArray[i]}")
        myArray.append((i+1)*2)


if __name__ == "__main__":
    main()
