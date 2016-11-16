""" Tests functions for ceaser.py """

import ceaser

def test_encode():
    """ Tests the encode function of the script """
    assert ceaser.encode("Eric", 3) == "Hulf"
