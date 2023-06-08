#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for arg in names:
        if arg[0] != "_" and arg[1] != "_":
            print("{}".format(arg))

else:
    pass
