""" Tests functions for ceaser.py """
#python

import ceaser

def test_encode():
    """ Tests the encode function of the script """
    assert ceaser.encode("Eric", 3) == "Hulf"

def test_decode():
    """ Tests the decode function of the script """
    assert ceaser.decode("Hulf", 3) == "Eric"
