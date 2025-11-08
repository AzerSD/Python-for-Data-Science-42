import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError more than one argument is provided")
        return 1
    elif len(sys.argv) < 2:
        return 1

    arg = sys.argv[1]
    if not (arg.isdigit() or (arg.startswith("-") and arg[1:].isdigit())):
        print("AssertionError: argument is not an integer")
        return 1

    num = int(arg)

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
