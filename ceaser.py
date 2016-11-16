"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution"""

import string

def encode(message, offset):
    """ Encode function """
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in message:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            pos = letters.index(letter) + offset
            encoded = encoded + letters[pos]

    return encoded
