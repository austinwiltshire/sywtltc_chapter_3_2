""" Tests functions for ceaser.py """

import ceaser

def test_encode(MESSAGE, OFFSET):
    """ Tests the encode function of the script """
    assert encode("Eric", 3) == "Hulf"
