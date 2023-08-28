'''When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"'''

import string


def position(alphabet):

    pos = string.ascii_lowercase.index(alphabet) + 1
    return f'Position of alphabet: {pos}'
