import sys
from ft_filter import ft_filter
import filterstring


def test_ft_filter():
    print("=== Testing ft_filter ===")

    # Test 1: Normal filtering
    result = ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
    print("Even numbers:", result)  # Expected: [2, 4, 6]

    # Test 2: Filtering with None (truthy items)
    result = ft_filter(None, [0, 1, False, True, "", "Hello"])
    print("Truthy values:", result)  # Expected: [1, True, 'Hello']

    # Test 3: Filtering characters in a string
    result = ft_filter(lambda c: c.lower() in "aeiou", "Hello World")
    print("Vowels in 'Hello World':", result)  # Expected: ['e', 'o', 'o']

    print()


def test_filterstring():
    print("=== Testing filterstring ===")

    # Save the original sys.argv
    original_argv = sys.argv.copy()

    # Test 1: Normal use
    sys.argv = ["filterstring.py", "aeiou", "Hello World"]
    print("Command:", sys.argv)
    filterstring.main()  # Expected: "eoo"

    # Test 2: Missing argument
    sys.argv = ["filterstring.py", "abc"]
    print("\nCommand:", sys.argv)
    filterstring.main()  # Expected: Error message about usage

    # Test 3: No common characters
    sys.argv = ["filterstring.py", "xyz", "Hello"]
    print("\nCommand:", sys.argv)
    filterstring.main()  # Expected: empty line (no match)

    # Restore original argv
    sys.argv = original_argv


if __name__ == "__main__":
    test_ft_filter()
    test_filterstring()
