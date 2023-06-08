#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
