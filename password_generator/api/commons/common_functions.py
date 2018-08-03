from random import choice, randint

from password_generator.utils.constants import CHANGE_LETTER_SIZE_CHANCE_IN_PERCENT


def apply_mappings(mappings: dict, used_words: list):
    """
    Applies character mappings defined in the request

    :param mappings: Character mappings -> Dictionary which contains character to replace,
        the list of characters which should be put and the replacement chance.
    :param used_words: Words used in the password.
    :return: The list of transformed words.
    """
    transformed_words = []

    for word in used_words:
        word_as_list = list(word)
        for mapping in mappings:
            mapped_character = mapping['character']
            distinct_characters = set(word)
            if mapped_character.upper() in distinct_characters:
                character_mappings = mapping['mapping']
                mapping_chance = mapping['chance']
                found_character_indices = __find_character_in_word(character=mapped_character.upper(), word=word)
                for idx in found_character_indices:
                    if randint(0, 100) <= mapping_chance:
                        word_as_list[idx] = choice(list(character_mappings))
        transformed_words.append("".join(word_as_list))
    return transformed_words


def apply_case(password_words, case_mode):
    """
    Applies the character casing rules on the password words.

    :param password_words: Words used to build the password.
    :param case_mode: Case mode. At the moment 3 rules are available:
        random - change the characters size randomly
        camel - use camelCase
        words - snake BUILT from WORDS :)
    :return: transformed password words.
    """
    case = {
        'random': __random_case,
        'camel': __camel_case,
        'words': __every_word_in_different_case
    }

    return case[case_mode](password_words)


def __find_character_in_word(character, word):
    return [i for i, ltr in enumerate(word) if ltr == character]


def __random_case(words):
    transformed_words = []
    for word in words:
        word_as_list = list(word)
        for index, character in enumerate(word_as_list):
            if randint(0, 100) >= CHANGE_LETTER_SIZE_CHANCE_IN_PERCENT:
                word_as_list[index] = word_as_list[index].lower()
        transformed_words.append("".join(word_as_list))
    return transformed_words


def __every_word_in_different_case(words):
    # even number indicates uppercase, lowercase otherwise
    case = randint(0, 1)
    transformed_words = []
    for word in words:
        if case % 2 == 0:
            transformed_words.append(word.upper())
        else:
            transformed_words.append(word.lower())
        case += 1
    return transformed_words


def __camel_case(words):
    transformed_words = []
    for word in words:
        w = list(word.lower())
        w[0] = w[0].upper()
        transformed_words.append("".join(w))
    return transformed_words
