from flask import Blueprint, jsonify, request
import logging

random_generator = Blueprint('random_generator', __name__)


@random_generator.route('/characters', methods=['POST'])
def random_generator_func():
    data = request.data
    logging.error(data)
    return jsonify({'test': 'test'})
