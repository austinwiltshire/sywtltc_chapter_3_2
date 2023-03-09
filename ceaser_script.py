#!/usr/bin/python

"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""

import string


def ceaser(choice, word):
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""
    if choice == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                x = letters.index(letter) + shift
                encoded = encoded + letters[x]
    if choice == "decode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                x = letters.index(letter) - shift
                encoded = encoded + letters[x]
    return encoded
