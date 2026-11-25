import importlib

module = importlib.import_module("Code.40_gcd")


def test_normal_numbers():
    assert module.find_gcd(12, 18) == 6


def test_equal_numbers():
    assert module.find_gcd(10, 10) == 10


def test_coprime_numbers():
    assert module.find_gcd(7, 9) == 1