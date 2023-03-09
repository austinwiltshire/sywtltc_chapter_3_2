"""Tests the ceaser cipher program."""
import ceaser_cipher


def test_ceaser_cipher():
    assert ceaser_cipher.ceaser('decode',ceaser_cipher.ceaser('encode','statement')) == 'not_statement'
