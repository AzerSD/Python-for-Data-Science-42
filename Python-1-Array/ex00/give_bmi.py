
def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Calculate BMI for given height and weight lists."""
    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list indicating if BMI values exceed the given limit."""
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("All BMI values must be integers or floats.")
    return [b > limit for b in bmi]


if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
