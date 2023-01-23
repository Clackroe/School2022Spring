# Built-in Data Structures in Python

## Lists

Lists in Python are similar to but easier than arrays in Java, as they are much more flexible. They can contain any type of data as their elements, and they can hold multiple types of data at the same time. Python lists are mutable, meaning that they can be modified after creation, and they are dynamic, meaning that they can grow and shrink in size as needed.

### Creating a List

To create an empty list, use the following syntax:

```python
emptyList = []

```

To create a list with initial, hardcoded values, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

```

### Accessing List Elements

Accessing elements in a list is similar to accessing elements in a standard array. Indexing starts at 0, and the last element in the list is at index -1. To access an element in a list, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

first_fruit = fruitList[0]

second_fruit = fruitList[1]

last_fruit = fruitList[-1]

```

### Modifying List Elements

We can directly modify an element at a specific index in a list. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList[0] = "orange"

```

### Adding Elements to a List

We can add elements to the end of a list using the `append()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.append("orange")

```

We can also add elements to a specific index in a list using the `insert()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.insert(1, "orange") # insert "orange" at index 1

```

Lists can also be concatenated using the `+` operator. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList = fruitList + ["orange", "kiwi"]

```

### Removing Elements from a List

We can remove elements from a list using the `remove()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.remove("banana")

```

We can also remove elements from a specific index in a list using the `pop()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.pop(1) # remove element at index 1

```

### Sorting a List

We can sort a list using the `sort()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.sort()

```

### Reversing a List

We can reverse a list using the `reverse()` method. To do this, use the following syntax:

```python
fruitList = ["apple", "banana", "cherry"]

fruitList.reverse()

```

## Tuples

Tuples in Python more closely resemble arrays in Java, as they are immutable and can only hold one type of data. Tuples are created using parentheses, and they can be accessed using square brackets. Tuples are immutable, so they cannot be modified after creation, but they are dynamic, meaning that they can grow and shrink in size as needed. These properties make tuples more efficient than lists, but you need to have a clear idea of what data is going to be stored in the tuple before you create it.

### Creating a Tuple

To create an empty tuple, use the following syntax:

```python
emptyTuple = ()

```

To create a tuple with initial, hardcoded values, use the following syntax:

```python
fruitTuple = ("apple", "banana", "cherry")

```

### Accessing Tuple Elements

Accessing elements in a tuple is similar to accessing elements in a standard array. Indexing starts at 0, and the last element in the tuple is at index -1. To access an element in a tuple, use the following syntax:

```python
fruitTuple = ("apple", "banana", "cherry")

first_fruit = fruitTuple[0]

second_fruit = fruitTuple[1]

last_fruit = fruitTuple[-1]

```

### Adding/Removing/Modifying Tuple Elements

Tuples are immutable, so they cannot be modified after creation. If you need to modify a tuple, you will need to create a new tuple with the modified values. To do this, use the following syntax:

```python
fruitTuple = ("apple", "banana", "cherry")

newTuple = fruitTuple + ("orange",)

```

Similarly, here's what the syntax looks like for removing the last element from a tuple and adding a new element to the end of the tuple:

```python
fruitTuple = ("apple", "banana", "cherry")

newTuple = fruitTuple[:-1] + ("orange",)

```

## Dictionaries

Dictionaries in Python are similar to maps in Java, as they are mutable and can hold multiple types of data. They rely on a key-value pair system, which requires each key to be unique. Dictionaries are mutable, meaning they can be modified after creation, and they are dynamic in size. Dictionaries have many built-in methods to handle common operations, but the syntax here is different from what we see with lists and tuples.

### Creating a Dictionary

To create an empty dictionary, use the following syntax:

```python
emptyDict = {}

```

To create a dictionary with initial, hardcoded values, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

```

### Accessing Dictionary Keys and Values from a Dictionary

By using square brackets and a known key, we can access the value associated with that key. To do this, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

apple_value = fruitDict["apple"]

```

### Adding New Key-Value Pairs to a Dictionary

To add a new key-value pair to a dictionary, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

fruitDict["orange"] = 4

```

### Deleting Key-Value Pairs from a Dictionary

To delete a key-value pair from a dictionary, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

del fruitDict["apple"]

```

### Modifying Values in a Dictionary

Updating the value associated with a key is simple. All we need to do is index in by the key and assign a new value to it. To do this, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

fruitDict["apple"] = 4

```

### Getting a List of Keys from a Dictionary

To get a list of keys from a dictionary, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

keys = fruitDict.keys()

```

### Getting a List of Values from a Dictionary

To get a list of values from a dictionary, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

values = fruitDict.values()

```

### Getting a List of Key-Value Pairs from a Dictionary as Tuples

To get a list of key-value pairs from a dictionary, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

items = fruitDict.items()

```

### Sorting a Dictionary by Its Keys

Sorting a dictionary by its keys is similar to sorting a list. To do this, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

sortedDict = sorted(fruitDict)

```

### Sorting a Dictionary by Its Values

Sorting a dictionary by its values is much trickier than by its keys. We will use something called a lamba function to accomplish this task. Lambda functions are a way to create a function on the fly, and they are often used to sort dictionaries in Python. In our lambda function, we will get the full list of dictionary tuples from the `.items()` method, and then we will sort them by the second element in each tuple. To do this, use the following syntax:

```python
fruitDict = {"apple": 1, "banana": 2, "cherry": 3}

sortedDict = sorted(fruitDict.items(), key=lambda x: x[1])

```

## Sets

Sets are very similar to lists in Python, but they are unordered and cannot contain duplicate elements. They are mutable (technically) and dynamic in size. This combination of properties makes them seem like a mixture of dictionaries and lists in Python, but remember that they do not have key-value pairs. Sets are created using curly braces, and they can be accessed using square brackets. These should be used when you need to store a collection of unique elements, but you do not need to access them by index or associate them with a key. Sets have one final restriction: they can only contain immutable elements. This means that you cannot add a list or a dictionary, but you can add a tuple, a string, or a number (int or float) to a set.

### Creating a Set

To create an empty set, use the following syntax:

```python
emptySet = set()

```

To create a set with initial, hardcoded values, use the following syntax:

```python
fruitSet = {"apple", "banana", "cherry"}

```

### Adding Elements to a Set

To add an element to a set, use the following syntax:

```python
fruitSet = {"apple", "banana", "cherry"}

fruitSet.add("orange")

```

### Removing Elements from a Set

To remove an element from a set, use the following syntax:

```python
fruitSet = {"apple", "banana", "cherry"}

fruitSet.remove("apple")

```

### Modifying Elements in a Set

Since sets are unordered, modifying elements is not possible, but we can simply remove the element and add a new one. To do this, use the following syntax:

```python
fruitSet = {"apple", "banana", "cherry"}

fruitSet.remove("apple")

fruitSet.add("orange")

```
