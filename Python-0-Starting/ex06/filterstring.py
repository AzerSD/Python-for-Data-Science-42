from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Usage: python filterstring.py \
                                 <substring> <string>")

        substring = sys.argv[1]
        string = sys.argv[2]

        filtered_chars = ft_filter(lambda x: x in substring, string)
        result = ''.join(filtered_chars)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
