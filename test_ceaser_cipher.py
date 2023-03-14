"""Tests the caesar cipher program."""

import caesar_cipher


def test_caesar_cipher():
    """This test uses the fact that f(g(x)) = x to test caesar_cipher"""
    assert caesar_cipher.caesar("decode", caesar_cipher.caesar("encode", "statement")) == "statement"
