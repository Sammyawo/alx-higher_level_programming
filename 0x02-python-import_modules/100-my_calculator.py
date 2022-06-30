#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def main():

    import sys
    for i in range(1, len(sys.argv)):
        if len(sys.argv) > 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        else:
            if len(sys.argv) == 1:
                a = sys.argv[i] 
            elif len(sys.argv) == 3:
                b = sys.argv[i]
            elif len(sys.argv) == 2:
                if sys.argv[i] == '+':
                    operator = sys.argv[i]
                    c = add(a, b)
                elif sys.argv[i] == '-':
                    operator = sys.argv[i]
                    c = sub(a, b)
                elif sys.argv[i] == '*':
                    operator = sys.argv[i]
                    c = mul(a, b)
                elif sys.argv[i] == '/':
                    operator = sys.argv[i]
                    c = div(a, b)
                else:
                    print("Unknown operator. Available operators: +, -, * and /")
                    exit(1)
            print("{} {} {} = {}".format(a, operator, b, c))


if __name__ == "__main__":
    main()
