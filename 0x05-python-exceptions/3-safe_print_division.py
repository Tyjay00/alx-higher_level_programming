def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
