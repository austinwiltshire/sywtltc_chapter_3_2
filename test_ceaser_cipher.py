"""Tests the ceaser cipher program."""
import ceaser_cipher


def test_ceaser_cipher():
    assert (
        ceaser_cipher.ceaser("decode", ceaser_cipher.ceaser("encode", "statement"))
        == "statement"
    )


li = [1, 2, 3, 4]
