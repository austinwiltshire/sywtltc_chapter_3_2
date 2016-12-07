"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution"""

import string

def encode(message, offset):
    """ Encode function """
    #assert isinstance(message) is str
    #assert isinstance(offset) is int
    if offset is None:
        pass
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in message:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            pos = letters.index(letter) + offset
            encoded = encoded + letters[pos]

    return encoded

def decode(encoded_message, offset):
    """ Decode function """
    assert encoded_message, "Please enter a message. There is nothing to decode!"
    assert offset, "Please enter an offset."
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in encoded_message:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            pos = letters.index(letter) - offset
            encoded = encoded + letters[pos]

    return encoded
