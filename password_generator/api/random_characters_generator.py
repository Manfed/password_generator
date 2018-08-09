from flask import Blueprint, jsonify, request
from random import randint

from safepass import safepass

from password_generator.metrics.entropy import count_entropy

random_generator = Blueprint('random_generator', __name__)


@random_generator.route('/characters', methods=['POST'])
def random_generator_func():
    """
    Create a password using random characters.
    ---
    tags:
        - Password from random characters
    parameters:
      - name: length
        in: body
        type: integer
        required: true
        description: Password length.
      - name: groups
        in: body
        type: array
        items:
            type: object
            properties:
                value:
                    type: string
        required: true
        description: Character groups using in password composition.
    responses:
      500:
        description: Internal Server Error.
      200:
        description: Password generated.
        schema:
          id: rcResponse
          properties:
            entropy:
              type: integer
              description: The entropy of the password.
            isSafe:
              type: boolean
              description: Password safety checked in the haveibeenpwned service.
            password:
              type: string
              description: Generated password.
        """
    effective_characters = set()
    effective_groups = []

    parsed_data = request.get_json()
    password_length = parsed_data['length']

    # remove redundant characters from groups
    for group in parsed_data['groups']:
        distinct_values = set(group['value']).difference(effective_characters)
        if len(distinct_values) > 0:
            effective_groups.append({'consumed': False, 'characters': distinct_values})
        effective_characters = effective_characters.union(distinct_values)

    password = __generate_password__(password_length=password_length, character_groups=effective_groups)
    return jsonify({'password': password,
                    'entropy': count_entropy(alphabet_length=len(effective_characters),
                                             password_length=password_length),
                    'isSafe': safepass(password)
                    })


def __generate_password__(password_length: int, character_groups: list) -> str:
    password = ''
    for i in range(password_length):
        if __should_shuffle_group__(groups=character_groups,
                                    remaining_password_letters=password_length - len(password)):
            used_group_index = randint(0, len(character_groups) - 1)
        else:
            used_group_index = __get_first_unused_group__(character_groups)
        character_group = character_groups[used_group_index]['characters']
        character_groups[used_group_index]['consumed'] = True
        password += list(character_group)[randint(0, len(character_group) - 1)]

    return password


def __should_shuffle_group__(groups: list, remaining_password_letters: int) -> bool:
    not_used_group_count = 0
    for group in groups:
        if not group['consumed']:
            not_used_group_count += 1
    if not_used_group_count == remaining_password_letters:
        return True
    else:
        return False


def __get_first_unused_group__(groups: list) -> int:
    for idx, group in enumerate(groups):
        if not group['consumed']:
            return idx
        else:
            return randint(0, len(groups) - 1)
