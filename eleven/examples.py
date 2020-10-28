def function_with_exception(val):
    """Return a `val` if it is non-negative"""
    if val < 0:
        raise ValueError("val cannot be negative.")

    return val

