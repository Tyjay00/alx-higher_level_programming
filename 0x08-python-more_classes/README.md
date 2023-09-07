# Python - More Classes and Objects

This project explores object-oriented programming in Python. It covers topics like class methods, static methods, class vs instance attributes, and special methods (`__str__` and `__repr__`).

## Table of Contents

- [Tests](#tests)
- [Tasks](#tasks)

---

## Tests :heavy_check_mark:

- [tests](./tests): Folder containing test files provided by Holberton School.

---

## Tasks :page_with_curl:

### Task 0: Simple Rectangle

- File: [0-rectangle.py](./0-rectangle.py)
- Description: An empty Python class that defines a rectangle.

### Task 1: Real Definition of a Rectangle

- File: [1-rectangle.py](./1-rectangle.py)
- Description: A Python class that defines a rectangle with:
  - Private instance attributes `width` and `height`.
  - Property getters and setters for `width` and `height`.
  - Instantiation with optional `width` and `height`, raising errors for invalid inputs.

### Task 2: Area and Perimeter

- File: [2-rectangle.py](./2-rectangle.py)
- Description: A Python class that extends the previous one with:
  - Public instance methods `area()` and `perimeter()` to calculate area and perimeter.
  - Proper handling of cases where `width` or `height` is 0.

### Task 3: String Representation

- File: [3-rectangle.py](./3-rectangle.py)
- Description: A Python class that extends the previous one with:
  - A special method `__str__` to print the rectangle using the `#` character.
  - Proper handling of cases where `width` or `height` is 0.

### Task 4: Eval is Magic

- File: [4-rectangle.py](./4-rectangle.py)
- Description: A Python class that extends the previous one with:
  - A special method `__repr__` to return a string representation of the rectangle.

### Task 5: Detect Instance Deletion

- File: [5-rectangle.py](./5-rectangle.py)
- Description: A Python class that extends the previous one with:
  - A special method `__del__` to print a message when a `Rectangle` instance is deleted.

### Task 6: How Many Instances

- File: [6-rectangle.py](./6-rectangle.py)
- Description: A Python class that extends the previous one with:
  - A public class attribute `number_of_instances` to track the number of instances created.
  - Incrementing and decrementing the attribute as instances are created and deleted.

### Task 7: Change Representation

- File: [7-rectangle.py](./7-rectangle.py)
- Description: A Python class that extends the previous one with:
  - A public class attribute `class_symbol` to customize the symbol used for string representation.

These tasks demonstrate various aspects of object-oriented programming in Python, including class structure, instance attributes, special methods, and class methods.
