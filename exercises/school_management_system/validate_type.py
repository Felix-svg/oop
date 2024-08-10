def validate_type(value, expected_type, name):
    if not isinstance(value, expected_type):
        raise ValueError(f"{name} must be of type {expected_type.__name__}")
    return value
