#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
        sys.exit(0)

    ps = "s" if argc > 1 else ""
    print("{} argument{}:".format(argc, ps))
    i = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
else:
    pass
