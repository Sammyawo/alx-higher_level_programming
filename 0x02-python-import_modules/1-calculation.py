#!/usr/bin/python3
def main():
    from calculation_1 import add, sub, mul, div


    a = 10
    b = 5
    result1 = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result1))

    result2 = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, result2))

    result3 = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, result3))

    result4 = div(a, b)
    print("{:d} / {:d} = {:.0f}".format(a, b, result4))


if __name__ == "__main__":
    main()
