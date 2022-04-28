#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    h = 0
    largo = len(sys.argv)

    for c in range(1, largo):
        h = h + int(sys.argv[c])

    print("{}".format(h))
