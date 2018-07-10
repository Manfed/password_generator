#!/usr/bin/env python

from flask import Flask
from flask_cors import CORS

from password_generator.api.random_characters_generator import random_generator

app = Flask(__name__)
CORS(app)

app.register_blueprint(random_generator, url_prefix='/random/')

def main():
    print("Started")
    app.run(port=8080, host='0.0.0.0')


if __name__ == "__main__":
    main()
