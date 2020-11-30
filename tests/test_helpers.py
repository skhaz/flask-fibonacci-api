import random

from app.helpers import safe_cast


def test_should_cast_simple_number():
    assert safe_cast("1234") == 1234


def test_should_return_none_on_a_non_number():
    assert safe_cast("abc1") is None


def test_should_cast_long_very_random_number():
    long_number = random.getrandbits(256)

    assert safe_cast(str(long_number)) == long_number
