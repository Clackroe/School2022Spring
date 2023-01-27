# Exercises on Object Oriented Programming in Python

## Introduction

In this brief exercise, you will be introduced to the core concepts of object oriented programming in Python. You will define classes, instantiate objects, and use inheritance to end up with elegant, reusable code. Like many of these exercises, this one will require you to read official Python documentation. Pay close attention to terms like `method`, `attribute`, and `class`. These will be used throughout the semester and your career as a software engineer, so it is crucial to understand the difference between these terms and `variable`, `function`, and `object`.

## Task 1: Methods

- Open the `person.py` file.
- Complete `TODO 1` by finishing the `get_greeting` method in the `Person` class so that it returns a string that says "Hello, my name is [name].".
- Complete `TODO 2` by finishing the `get_age` method in the `Person` class so that it returns the age of the person.
  - **TIP:** Official documentation for the built-in `datetime.date` class can be found [here](https://docs.python.org/3/library/datetime.html#datetime.date).
- Check your work by running the `person.py` file.

## Task 2: Creating Classes and Basic Inheritance

- Open the `student.py` file.
- Complete `TODO 3` by starting the constructor for the `Student` class.
- Complete `TODO 4` by using the `super` function to call the `Person` constructor from the `Student` constructor.
  - **TIP:** Official documentation for the built-in `super` function can be found [here](https://docs.python.org/3/library/functions.html#super).
- Complete `TODO 5` by initializing the `student_id` and `credit_hours` attributes in the `Student` constructor.
- Complete `TODO 6` by adding a new method to the `Student` class called `get_student_id` that returns the student's ID.
- Complete `TODO 7` by adding a new method to the `Student` class called `calculate_workload` that returns the number of hours the student is taking multiplied by 3.
- Check your work by running the `student.py` file.

## Task 3: Inheritance and Polymorphism

- Open the `software.py` file.
- Complete `TODO 8` by importing the `Student` class from the `student.py` file.
- Complete `TODO 9` by creating a new class called `SoftwareStudent` that inherits from the `Student` class. Follow the instructions in the comments for the class definition details. This step is just like you did in Task 2, but with a new class.
- Complete `TODO 10` by adding a new method to the `SoftwareStudent` class called `get_major` that returns the student's major.
- Complete `TODO 11` by updating the `get_greeting` method in the `SoftwareStudent` class so that it returns a string that says "Hello, my name is [name] and I am a [major] major."
- Complete `TODO 12` by updating the `calculate_workload` method in the `SoftwareStudent` class so that it returns the number of hours the student is taking multiplied by 2.

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire `oop` directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal on Mac or Linux machines: `zip -r -X dgary9.zip .`
    - **TIP:** For Windows users who want to use their terminal to zip their submission, you can use the `7z` command. Here's an example of how to do it: `7z a dgary9.zip .`
    - **NOTE:** In the above examples, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`oop`) in this case.
