import json
import re

from collections import defaultdict
from flask import Blueprint, jsonify, request, abort
from PyLyrics import PyLyrics
from random import choice, randint, shuffle

from safepass import safepass

from password_generator.api.commons.common_functions import apply_mappings, apply_case
from password_generator.database.database import db_session
from password_generator.database.model.album import Album as DbAlbum
from password_generator.metrics.entropy import count_entropy, count_alphabet_size

random_words_from_song_generator = Blueprint('random_generator_from_songs', __name__)


@random_words_from_song_generator.errorhandler(UnboundLocalError)
def handle_invalid_artist(error):
    response = jsonify({
        'error': error.args,
        'message': 'Unknown artist. Check the artist name and ensure that artist is present on http://lyrics.wikia.com',
        'status_code': 404,
        'reason': 'Artist or songs not found.'
    })
    response.status_code = 404
    return response


@random_words_from_song_generator.route('/song', methods=['POST'])
def generate_password_from_song_lyrics():
    """
    Create a password using song lyrics.
    ---
    tags:
        - Password from song lyrics
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
      - name: artist
        in: body
        type: string
        required: true
        description: Artist who's song will be used.
    responses:
      500:
        description: Internal Server Error.
      404:
        description: Song not found.
      200:
        description: Password generated.
        schema:
          id: rwfsResponse
          properties:
            password_words:
              type: array
              items:
                type: string
              description: Modified password words.
            entropy:
              type: integer
              description: The entropy of the password.
            used_words:
              type: array
              items:
                type: string
              description: Words used to create a password.
            isSafe:
              type: boolean
              description: Password safety checked in the haveibeenpwned service.
            lyrics:
              type: string
              description: Song's lyrics.
            song_name:
              type: string
              description: Song name.
    """
    data = request.get_json()

    password_length = data['passwordLength']
    mappings = data['mappings']
    case_mode = data['rwCase']
    artist = data['artist']

    albums = __get_albums(artist)

    if albums is not None:
        album = choice(albums)
        track = choice(album.tracks())
        lyrics = track.getLyrics()
        used_words = __choose_words_from_lyrics(lyrics, password_length)

        password_words = apply_mappings(mappings, used_words)
        password_words = apply_case(password_words, case_mode)

        password = ''.join(password_words)

        return jsonify({
            'used_words': used_words,
            'password_words': password_words,
            'entropy': count_entropy(count_alphabet_size(password), len(password)),
            'lyrics': lyrics,
            'song_name': track.name,
            'isSafe': safepass(password)
        })
    else:
        abort(404)


def __get_albums(artist):
    album = __get_album_from_db(artist)
    if album is None:
        return __get_album_from_wikia(artist)
    return album


def __get_album_from_db(artist):
    albums = db_session \
        .query(DbAlbum.artist) \
        .filter(DbAlbum.artist == artist) \
        .first()
    if albums is None:
        return None
    else:
        return json.load(albums)


def __get_album_from_wikia(artist):
    return PyLyrics.getAlbums(singer=artist)


def __choose_words_from_lyrics(lyrics, password_length):
    """
    Chooses random words from the song lyrics.

    :param lyrics: song lyrics
    :param password_length: targeted password length
    :return: a list of used words and the number of distinct words in the song
    """
    used_words = []
    remained_characters = password_length
    cleaned_lyrics = set(re.sub("[^\w]", " ", lyrics).upper().split())

    distinct_words_by_length = defaultdict(list)
    for word in cleaned_lyrics:
        distinct_words_by_length[len(word)].append(word)

    min_word_length = min(distinct_words_by_length.keys())
    max_word_length = max(distinct_words_by_length.keys())

    while remained_characters > 0:
        word_length = randint(min_word_length, min(max_word_length, remained_characters))
        if word_length == password_length:
            word_length = randint(min_word_length, word_length - min_word_length)
        if word_length in distinct_words_by_length:
            used_words.append(choice(distinct_words_by_length[word_length]))
            remained_characters -= word_length
    shuffle(used_words)
    return used_words
