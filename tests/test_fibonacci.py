import pytest

from app.fibonacci import fibonacci, is_valid


def test_should_compute_fibonacci_of_0_correctly():
    assert fibonacci(0) == 0


def test_should_compute_fibonacci_of_1_correctly():
    assert fibonacci(1) == 1


def test_should_compute_fibonacci_of_2_correctly():
    assert fibonacci(2) == 1


def test_should_compute_fibonacci_of_3_correctly():
    assert fibonacci(3) == 2


def test_should_compute_fibonacci_of_10_correctly():
    assert fibonacci(10) == 55


def test_should_compute_fibonacci_of_100_correctly():
    assert fibonacci(100) == 354224848179261915075


def test_should_handle_negative_number():
    assert fibonacci(-1) == -1


def test_should_return_false_if_number_is_none():
    assert is_valid(None) == False


def test_should_return_false_if_number_is_negative():
    assert is_valid(-1) == False


def test_should_return_false_if_number_is_greater_than_100():
    assert is_valid(101) == False


def test_should_return_true_if_number_is_less_than_100_and_greater_than_0():
    assert is_valid(10) == True
