def gender_selector(name):
    if not isinstance(name, str):
        raise ValueError("not a string")

    if name.lower() in ["anna", "beata", "cecylia"]:
        return "F"
    elif name.lower() in ["piotr", "bartosz"]:
        return "M"
    else:
        return "unknown"
