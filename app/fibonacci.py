import functools


@functools.lru_cache(None)
def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def is_valid(number):
    if number is None:
        return False

    if number < 0:
        return False

    if number > 100:
        return False

    return True
