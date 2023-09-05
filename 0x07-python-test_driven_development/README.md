# Python - Test-driven development

In this project, I started practicing test-driven development using `docstring`
and `unittest` in Python.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the
following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

1. **Integers Addition (0-add_integer.py)**
   - Function: `def add_integer(a, b=98):`
   - Description: This function returns the integer addition of two numbers, with type checks.

2. **Divide a Matrix (2-matrix_divided.py)**
   - Function: `def matrix_divided(matrix, div):`
   - Description: Divides all elements of a matrix by a common divisor, with error handling.

3. **Say My Name (3-say_my_name.py)**
   - Function: `def say_my_name(first_name, last_name=""):`
   - Description: Prints a name in the format `My name is <first_name> <last_name>`, with type checks.

4. **Print Square (4-print_square.py)**
   - Function: `def print_square(size):`
   - Description: Prints a square using the `#` character, with size validation.

5. **Text Indentation (5-text_indentation.py)**
   - Function: `def text_indentation(text):`
   - Description: Prints text with specific indentation rules, with type checks.

6. **Max Integer - Unittest (tests/6-max_integer_test.py)**
   - Description: Unit tests for the provided `max_integer` function.

7. **Matrix Multiplication (100-matrix_mul.py)**
   - Function: `def matrix_mul(m_a, m_b):`
   - Description: Performs matrix multiplication, with error handling.

8. **Lazy Matrix Multiplication (101-lazy_matrix_mul.py)**
   - Function: `def lazy_matrix_mul(m_a, m_b):`
   - Description: Performs matrix multiplication using the NumPy library, similar to the previous task.

9. **CPython #3: Python Strings (102-python.c)**
   - Function: `void print_python_string(PyObject *p);`
   - Description: A C function that prints information about Python string objects.
