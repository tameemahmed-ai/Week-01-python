"""
Simple jacket advisor: reads Fahrenheit and recommends what to wear.

Invalid input (letters, empty string) is handled with try/except so the program
does not crash.
"""


def should_wear_jacket(temp_f: float) -> str:
    """Return clothing advice for the given temperature in Fahrenheit."""
    if temp_f < 60:
        return "Yes, wear a jacket! It's cold."
    if temp_f < 70:
        return "Maybe bring a light jacket."
    return "No jacket needed, enjoy the weather!"


def read_temperature_fahrenheit() -> float:
    """
    Ask for temperature until the user enters something that can be parsed as a float.

    `float("hello")` raises ValueError — we catch it and ask again instead of crashing.
    """
    while True:
        raw = input("What's the temperature in Fahrenheit? ").strip()
        try:
            return float(raw)
        except ValueError:
            # Not a valid number: could be text, symbols, or empty after strip edge cases
            print("Please type a number only (for example: 72 or 55.5).")


def main() -> None:
    temp = read_temperature_fahrenheit()
    print(should_wear_jacket(temp))


if __name__ == "__main__":
    main()
