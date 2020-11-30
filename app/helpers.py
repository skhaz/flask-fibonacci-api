def safe_cast(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default
