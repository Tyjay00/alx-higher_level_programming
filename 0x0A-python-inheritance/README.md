# Python - Inheritance

In this project, I explored Python class inheritance, delving into the distinctions between super- and sub-classes. I practiced creating classes with multiple base classes, and I also honed my skills in overriding inherited methods and attributes.

## Tests :heavy_check_mark:

* [tests](./tests): This folder contains test files:
    * [1-my_list.txt](./1-my_list.txt)
    * [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Here are the prototypes for the functions I implemented in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Tasks :page_with_curl:

* **0. Lookup**
  * [0-lookup.py](./0-lookup.py): This Python function returns a list of available attributes and methods of an object.

* **1. My list**
  * [1-my_list.py](./1-my_list.py): In this task, I created a Python class called `MyList`, which inherits from `list`. This class includes a public instance method, `def print_sorted(self):`, which prints the list in ascending sorted order, assuming all list elements are `int`s.

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py): I implemented a Python function that returns `True` if an object is exactly an instance of a specified class; otherwise, it returns `False`.

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): This Python function returns `True` if an object is an instance of a specified class or has inherited from that class; otherwise, it returns `False`.

* **4. Only sub class of**
  * [4-inherits_from.py](./4-inherits_from.py): I created a Python function that returns `True` if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise, it returns `False`.

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py): In this task, I introduced an empty Python class called `BaseGeometry`.

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py): I enhanced the `BaseGeometry` class from the previous task by adding a public instance method, `def area(self):`, which raises an `Exception` with the message `area() is not implemented`.

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry.py): Building upon the previous tasks, I expanded the `BaseGeometry` class with a public instance method, `def integer_validator(self, name, value):`, that validates the parameter `value`. It assumes that the parameter `name` is always a string. If the `value` is not an `int`, a `TypeError` exception is raised with the message `<name> must be an integer`. If the `value` is not greater than `0`, a `ValueError` exception is raised with the message `<value> must be greater than 0`.

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py): I introduced a Python class called `Rectangle`, which inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). This class includes private attributes `width` and `height`, both of which are validated with the `integer_validator` method. The class can be instantiated with `width` and `height` values using `def __init__(self, width, height):`.

* **9. Full rectangle**
  * [9-rectangle.py](./9-rectangle.py): In this task, I extended the `Rectangle` class from the previous task by implementing the `area()` method and adding a special method, `__str__`, to print `Rectangle` objects in the format `[Rectangle] <width>/<height>`.

* **10. Square #1**
  * [10-square.py](./10-square.py): I created a Python class called `Square`, which inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). This class includes a private attribute, `size`, which is validated with the `integer_validator` method. It can be instantiated with a `size` using `def __init__(self, size):`, and it implements the `area()` method.

* **11. Square #2**
  * [11-square.py](./11-square.py): Building upon the previous task, I added a special method, `__str__`, to the `Square` class to print square objects in the format `[Square] <width>/<height>`.

* **12. My integer**
  * [100-my_int.py](./100-my_int.py): In this task, I created a Python class called `MyInt`, which inherits from `int`. The class includes the inversion of the `==` and `!=` operators.

* **13. Can I?**
  * [101-add_attribute.py](./101-add_attribute.py): I implemented a Python function that adds a new attribute to an object if possible. If adding the attribute is not possible, it raises a `TypeError` exception with the message `can't add new attribute`.
