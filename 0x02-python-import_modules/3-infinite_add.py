#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0")
        sys.exit(0)

    sum = 0
    for arg in sys.argv[1:]:
        sum += int(arg)
    print("{}".format(sum))

else:
    pass
