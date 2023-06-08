#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]

    if op == "+":
        print("{} {} {} = {}".format(num1, num2, op, add(num1, num2)))
    elif op == "-":
        print("{} {} {} = {}".format(num1, num2, op, sub(num1, num2)))
    elif op == "*":
        print("{} {} {} = {}".format(num1, num2, op, mul(num1, num2)))
    elif op == "/":
        print("{} {} {} = {}".format(num1, num2, op, div(num1, num2)))
    else:
        print("Unknown opator. Available opators: +, -, * and /")
        sys.exit(1)

else:
    pass
