"""Hardened Password Policy Module.

Defensively handles all unexpected, empty, or malformed inputs discovered
via Hypothesis property-based fuzz testing.

Author: N. Adil Ahmed (PES1UG24CS285)
Lab 7: Fuzzing for Input Validation Bugs
"""


def first_character_type(pw):
    """Classify the type of the first character in pw.

    Returns 'digit', 'letter', 'symbol', or 'empty' for missing/empty inputs.
    """
    if not isinstance(pw, str) or len(pw) == 0:
        return "empty"
    ch = pw[0]
    if ch.isdigit():
        return "digit"
    if ch.isalpha():
        return "letter"
    return "symbol"


def split_credentials(text):
    """Split credentials string into (username, password).

    Defensively handles:
    - None or non-string inputs
    - Strings without a colon
    - Strings with multiple colons
    """
    if not isinstance(text, str) or not text:
        return "", ""
    if ":" not in text:
        return text.strip(), ""
    parts = text.split(":", 1)
    return parts[0].strip(), parts[1].strip()


def digit_ratio(pw):
    """Calculate the proportion of numeric digits in pw (0.0 to 1.0).

    Defensively guards against:
    - None or non-string inputs
    - Empty strings (avoids ZeroDivisionError)
    """
    if not isinstance(pw, str) or len(pw) == 0:
        return 0.0
    return sum(c.isdigit() for c in pw) / len(pw)


def main():
    """Interactive command-line demonstration for testing."""
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    print("First Character Type:", result)

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    print("User and Password:", result)

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result)


if __name__ == "__main__":
    main()
