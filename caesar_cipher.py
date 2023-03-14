#!/usr/bin/python

"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""

import string


def caesar(choice, word):
    """
    This function writes a caesar cipher
    :param choice: Either 'encode' or 'decode'
    :param word: the statement to be ""coded
    :return: returns encoded word if encoded and vice versa
    """
    shift = 3
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""
    if choice == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                index: int = letters.index(letter) + shift
                encoded = encoded + letters[index]
    if choice == "decode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                index = letters.index(letter) - shift
                encoded = encoded + letters[index]
    return encoded
