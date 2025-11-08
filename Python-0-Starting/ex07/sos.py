import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    """Converts a string to Morse code."""
    try:
        if len(sys.argv) != 2 or not sys.argv[1].isalnum():
            raise AssertionError("AssertionError: the arguments are bad")

        input_string = sys.argv[1].upper()
        morse_code = ""

        for char in input_string:
            if char in NESTED_MORSE:
                morse_code += NESTED_MORSE[char]
            else:
                raise AssertionError("AssertionError: the arguments are bad")

        print(morse_code.strip())
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
