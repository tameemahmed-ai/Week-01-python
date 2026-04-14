"""
Command-line weather advisor: reads Fahrenheit and suggests whether to wear a jacket.
"""

# Below this temperature (°F), light outerwear is generally a good idea for most people.
JACKET_THRESHOLD_F: float = 60.0


def needs_jacket(temp_fahrenheit: float) -> bool:
    """
    Return True if the temperature suggests wearing a jacket.

    Uses a single threshold; adjust JACKET_THRESHOLD_F if you prefer stricter or looser advice.
    """
    return temp_fahrenheit < JACKET_THRESHOLD_F


def weather_recommendation(temp_fahrenheit: float) -> str:
    """Build a short recommendation string based on temperature and jacket need."""
    if needs_jacket(temp_fahrenheit):
        return (
            f"At {temp_fahrenheit:.1f}°F, it is cool enough that a jacket or light layer "
            "is a good idea."
        )
    return (
        f"At {temp_fahrenheit:.1f}°F, it is mild; you can skip the jacket "
        "(dress for your own comfort)."
    )


def read_temperature_fahrenheit() -> float:
    """
    Prompt until the user enters a valid number (interpreted as Fahrenheit).

    try / except: if the user types non-numeric text, float() raises ValueError.
    Catching it lets us print a hint and ask again instead of exiting with a traceback.
    """
    while True:
        raw = input("Enter temperature in Fahrenheit: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number (e.g. 72 or 32.5).")


def main() -> None:
    temp_f = read_temperature_fahrenheit()
    print(weather_recommendation(temp_f))


if __name__ == "__main__":
    main()
