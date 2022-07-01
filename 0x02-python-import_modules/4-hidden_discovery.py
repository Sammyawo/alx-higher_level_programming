#!/usr/bin/python3


def main():
    for p in dir(hidden_4):
        if p[0] != '_' and p[1] != '_':
            print("{}".format(p))


if __name__ == "__main__":
    import hidden_4
    main()
