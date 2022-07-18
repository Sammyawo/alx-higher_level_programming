#!/usr/bin/python3
def safe_print_division(a, b):
    p = 0.0
    s = 0
    try:
        p = a / b
        s = 1
    except ZeroDivisionError:
        pass
    finally:
        if s == 1:
            print("Inside result: {}".format(p))
            return p
        else:
            print("Inside result: {}".format(None))
            return None
