from math import ceil

from decimal import Decimal

from password_generator.metrics.entropy import count_alphabet_size, count_entropy
from password_generator.utils.constants import PASSWORD_CRACK_TRIES_PER_SECOND


def count_cracking_time(password: str):
    """
    Counts time in years needed to crack the password.

    :param password: Password which time will be counting for.
    :return: Time in years.
    """
    alphabet_size = count_alphabet_size(password)
    entropy = count_entropy(alphabet_size, len(password))

    return count_cracking_time_for_entropy(entropy)


def count_cracking_time_for_entropy(entropy: int):
    time_in_seconds = 2 ** entropy / PASSWORD_CRACK_TRIES_PER_SECOND

    return '%.2E' % Decimal(ceil(time_in_seconds / 60 / 60 / 24 / 365.25))
