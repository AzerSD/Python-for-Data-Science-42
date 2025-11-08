
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
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


