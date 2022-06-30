#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def main():

    import sys
    if len(sys.argv) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if len(sys.argv) == 1:
            a = int(sys.argv[1]) 
        elif len(sys.argv) == 3:
            b = int(sys.argv[3])
        elif len(sys.argv) == 2:
            if sys.argv[2] == '+':
                operator = sys.argv[2]
                c = add(a, b)
            elif sys.argv[2] == '-':
                operator = sys.argv[2]
                c = sub(a, b)
            elif sys.argv[2] == '*':
                operator = sys.argv[2]
                c = mul(a, b)
            elif sys.argv[2] == '/':
                operator = sys.argv[2]
                c = div(a, b)
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
        print("{} {} {} = {}".format(a, operator, b, c))


if __name__ == "__main__":
    main()
