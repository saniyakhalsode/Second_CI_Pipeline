import importlib

module = importlib.import_module("Code.34_check_sorted")


def test_sorted_array():
    assert module.is_sorted([1, 2, 3, 4, 5]) is True


def test_unsorted_array():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_empty_array():
    assert module.is_sorted([]) is True