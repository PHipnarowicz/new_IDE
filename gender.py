def gender_selector(name):
    if not isinstance(name, str):
        raise ValueError("not a string")

    if name in ["Anna", "Beata", "Cecylia"]:
        return "F"
    elif name in ["Piotr", "Bartosz"]:
        return "M"
    else:
        return "unknown"
