from math import log2, ceil
from re import sub

from password_generator.utils.constants import LATIN_CAPITAL_LETTERS, POLISH_CAPITAL_LETTERS, LATIN_SMALL_LETTERS, \
    POLISH_SMALL_LETTERS, DIGITS, SPECIAL_CHARACTERS


def count_entropy(alphabet_length, password_length):
    entropy = log2(alphabet_length)
    return ceil(entropy) * password_length


def count_alphabet_size(password: str):
    alphabet_size = 0
    character_sets = [
        LATIN_CAPITAL_LETTERS,
        LATIN_SMALL_LETTERS,
        POLISH_CAPITAL_LETTERS,
        POLISH_SMALL_LETTERS,
        DIGITS,
        SPECIAL_CHARACTERS
    ]
    tmp_password = password
    for character_set in character_sets:
        tmp = sub(character_set, '', tmp_password)
        if len(tmp) < len(tmp_password):
            alphabet_size += len(character_set)
            tmp_password = tmp
    alphabet_size += len(tmp_password)
    return alphabet_size
