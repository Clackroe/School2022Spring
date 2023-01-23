# Built-in Keywords in Python

These are common keywords that are built into Python. They are used to perform specific operations, and they are reserved words that cannot be used as variable names. Each one will be useful for assignments and general Python programming, so it's important to know what they do.

## `print()`

You almost certainly know this one already, but it's important to know that it's a keyword. The `print()` function prints the specified message to the screen, or other standard output device. To use it, simply pass in the message as an argument, and it will print the message to the screen.

```python

print("Hello, World!")
```

We can also give a default end value to the `print()` function. This will be the value that is printed at the end of the message. By default, this is a newline character, but we can change it to whatever we want. To use it, simply pass in the message and the end value as arguments, and it will print the message to the screen with the end value at the end.

```python
print("Hello, World!", end=" ") # this will print "Hello, World! " instead of "Hello, World!"

print("Hello, World!", end="!") # this will print "Hello, World!!" instead of "Hello, World!"
```

## `input()`

The `input()` function allows user input. To use it, simply pass in the prompt as an argument, and it will print the prompt to the screen and wait for user input. It will then return the user input as a string.

```python
name = input("What is your name? ")

print("Hello, " + name + "!")
```

## `len()`

The `len()` function returns the length of a list, tuple, or string, and is used to determine the number of elements in the given object. To use it, simply pass in the object as an argument, and it will return the number of elements in the object.

```python
fruitList = ["apple", "banana", "cherry"]

print(len(fruitList))
```

## `range()`

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. To use it, simply pass in the number you want to stop at as an argument, and it will return a sequence of numbers from 0 to the number you passed in.

```python
for i in range(5):
    print(i)
```

## `sorted()`

The `sorted()` function returns a sorted list from the elements in an iterable. To use it, simply pass in the iterable as an argument, and it will return a sorted list of the elements in the iterable.

```python
fruitList = ["banana", "apple", "cherry"]

print(sorted(fruitList))
```

## `sum()`

The `sum()` function can be used to add all the elements in a list or tuple. This requires that all the elements in the list or tuple are numbers. To use it, simply pass in the list or tuple as an argument and receive the returned value.

```python
numList = [1, 2, 3]

print(sum(numList)) # this would be 6
```

## `type()`

The `type()` function returns the type of the object passed into it. To use it, simply pass in the object as an argument, and it will return the type of the object.

```python

print(type(1)) # this would be int
print(type(1.0)) # this would be float
print(type("1")) # this would be str
print(type([1, 2, 3])) # this would be list
print(type((1, 2, 3))) # this would be tuple
print(type({"apple": 1, "banana": 2, "cherry": 3})) # this would be dict
print(type({"apple", "banana", "cherry"})) # this would be set
```

## `zip()`

The `zip()` function returns an iterator of tuples based on the iterable objects. To use it, simply pass in the iterable objects as arguments, and it will return an iterator of tuples based on the iterable objects.

```python
fruitList = ["apple", "banana", "cherry"]
numList = [1, 2, 3]

print(zip(fruitList, numList))
```
