from flask import Blueprint, jsonify, request
from random import randint, random, shuffle

from safepass import safepass
from sqlalchemy import func

from password_generator.api.commons.common_functions import apply_mappings, apply_case
from password_generator.database.database import db_session
from password_generator.database.model.word import Word
from password_generator.metrics.cracking_time import count_cracking_time
from password_generator.metrics.entropy import count_entropy, count_alphabet_size

random_words_generator = Blueprint('random_words_generator', __name__)


@random_words_generator.route('/words', methods=['POST'])
def random_words_func_post():
    """
    Create a password using random words.
    ---
    tags:
        - Password from random words
    parameters:
      - name: passwordLength
        in: body
        type: integer
        required: true
        description: Password length.
      - name: mappings
        in: body
        type: array
        items:
            type: object
            properties:
                character:
                    type: string
                mapping:
                    type: string
                chance:
                    type: integer
        required: true
        description: Character mapping rules.
      - name: rwCase
        in: body
        type: string
        enum: [random, camel, words]
        required: true
        description: Words case strategy.
    responses:
      500:
        description: Internal Server Error.
      200:
        description: Password generated.
        schema:
          id: rwResponse
          properties:
            passwordWords:
              type: array
              items:
                type: string
              description: Modified password words.
            crackingTime:
              type: integer
              description: Time needed to crack the password.
            usedWords:
              type: array
              items:
                type: string
              description: Words used to create a password.
            isSafe:
              type: boolean
              description: Password safety checked in the haveibeenpwned service.
    """
    data = request.get_json()

    password_length = data['passwordLength']
    mappings = data['mappings']
    case_mode = data['rwCase']

    max_word_length = db_session.query(Word.length, func.max(Word.length)).first()[0]
    min_word_length = db_session.query(Word.length, func.min(Word.length)).first()[0]

    used_words = __choose_random_words(max_word_length=max_word_length,
                                                 min_word_length=min_word_length,
                                                 password_length=password_length)

    password_words = apply_mappings(mappings, used_words)
    password_words = apply_case(password_words=password_words, case_mode=case_mode)

    password = ''.join(password_words)
    return jsonify({
        'passwordWords': password_words,
        'crackingTime': count_cracking_time(password),
        'usedWords': used_words,
        'isSafe': safepass(password)
    })


def __choose_random_words(max_word_length, min_word_length, password_length):
    used_words = []
    remaining_letters = password_length

    while remaining_letters >= min_word_length:
        random_word_length = randint(min_word_length,
                                     min([remaining_letters, max_word_length]))
        if random_word_length == password_length:
            random_word_length = randint(min_word_length, random_word_length - min_word_length)
        remaining_letters = __add_random_word_to_password(random_word_length, remaining_letters, used_words)
    if remaining_letters > 0:
        rest = max([remaining_letters, min_word_length])
        __add_random_word_to_password(rest, remaining_letters, used_words)

    shuffle(used_words)
    return used_words


def __add_random_word_to_password(random_word_length, remaining_letters, used_words):
    random_word = __get_random_word_with_length(random_word_length)
    used_words.append(random_word)
    remaining_letters -= random_word_length
    return remaining_letters


def __get_random_word_with_length(length):
    query = db_session.query(Word.word).filter(Word.length == length)
    row_count = int(query.count())
    return query.offset(int(row_count * random())).first()[0]
