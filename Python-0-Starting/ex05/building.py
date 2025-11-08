import sys


def main():
    """
        This program analyzes a given text
        (from command line argument or standard input)
        and counts the number of characters,
        uppercase letters, lowercase letters,
        spaces, digits, and punctuation marks.
    """

    if len(sys.argv) > 2:
        print("AssertionError: Please enter 1 text")
        return

    if len(sys.argv) != 2:
        print("Please enter some text (press Ctrl+D to finish):")
        text = ""
        last_line = ""
        try:
            while True:
                line = input()
                last_line = line
        except EOFError:
            text = last_line if last_line else ""
    else:
        text = sys.argv[1]

    print(f"The text contains {len(text)} characters.")

    upper = 0
    lower = 0
    space = 0
    digit = 0
    punkt = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        elif char in '''!?,.-;:''':
            punkt += 1

    print(f"{upper} uppercase letters")
    print(f"{lower} lowercase letters")
    print(f"{punkt} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    main()
