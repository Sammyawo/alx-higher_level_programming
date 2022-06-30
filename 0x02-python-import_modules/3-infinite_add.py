#!/usr/bin/python3
def main():
    j = 0
    for i in range(1, len(sys.argv)):
        j = sys.argv + j

    print("{:d}".format(j), end="")


if __name__ == "__main__":
    import sys
    main()
