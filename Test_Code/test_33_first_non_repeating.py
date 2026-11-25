import importlib

module = importlib.import_module("Code.33_first_non_repeating")


def test_normal_string():
    assert module.first_non_repeating("aabbcde") == "c"


def test_first_character():
    assert module.first_non_repeating("abcabcx") == "x"


def test_all_repeating():
    assert module.first_non_repeating("aabbcc") is None