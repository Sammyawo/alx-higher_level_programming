#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    p = 0.0
    k = []
    s = 0
    for i in range(0, list_length):
        try:
            p = my_list_1[i] / my_list_2[i]
            s = 1
        except ZeroDivisionError:
            print("division by 0")
            k += [0]
        except (ValueError, TypeError):
            print("wrong type")
            k += [0]
        except IndexError:
            print("out of range")
            k += [0]
        finally:
            if s == 1:
                s = 0
                k += [p]
    return k
