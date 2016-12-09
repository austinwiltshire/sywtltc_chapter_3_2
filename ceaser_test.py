""" Tests functions for ceaser.py """
#python

import ceaser

def test_encode():
    """ Tests the encode function of the script """
    assert ceaser.encode("Eric", 3) == "Hulf"
    assert ceaser.encode("P a", 3) == "S d"
    assert ceaser.encode("Z", 2) == '"'
    assert ceaser.encode("z", 2) == "B"
    assert ceaser.encode("DE", -2) == "BC"
    assert ceaser.encode("2", 4) == "6"
    assert ceaser.encode("(", 3) == "+"

def test_decode():
    """ Tests the decode function of the script """
    assert ceaser.decode("Hulf", 3) == "Eric"
    assert ceaser.decode("S d", 3) == "P a"
    assert ceaser.decode('"', 2) == "Z"
    assert ceaser.decode("B", 2) == "z"
    assert ceaser.decode("BC", -2) == "DE"
    assert ceaser.decode("6", 4) == "2"
    assert ceaser.decode("+", 3) == "("
