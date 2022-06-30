#!/usr/bin/python3
import sys

def main():
    j = 0
    for i in range(1, len(sys.argv)):
        j += sys.argv[i]

    print("{}".format(j), end="")


if __name__ == "__main__":
    main()
