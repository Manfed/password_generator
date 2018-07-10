from math import log2, ceil


def count_entropy(alphabet_length, password_length):
    entropy = log2(alphabet_length)
    return ceil(entropy) * password_length
