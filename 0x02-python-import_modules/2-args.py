#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    largo = len(sys.argv)
    if largo == 2:
        print("1 argument:")
    elif largo == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(largo - 1))

    if len(sys.argv) > 1:
        for c in range(1, largo):
            print("{}: {}".format(c, sys.argv[c]))
