import importlib

module = importlib.import_module("Code.37_rotate_string")


def test_normal_rotation():
    assert module.rotate_string("Python", 2) == "thonPy"


def test_full_rotation():
    assert module.rotate_string("Hello", 5) == "Hello"


def test_empty_string():
    assert module.rotate_string("", 2) == ""