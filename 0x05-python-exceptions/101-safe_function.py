#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    m = "Exception: division by zero\n"
    z = "Exception: list index out of range\n"
    try:
        return(fct(*args))
    except ZeroDivisionError as m:
        print("Exception: {}".format(m), file=sys.stderr)
    except IndexError as z:
        print("Exception: {}".format(z), file=sys.stderr)
