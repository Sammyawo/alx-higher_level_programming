#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    p = False
    m = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        p = True
    except (ValueError, TypeError) as m:
        print("Exception: {}".format(m), file=sys.stderr)
    return p
