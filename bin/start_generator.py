#!/usr/bin/env python

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from password_generator.api.test_module import test_module
from password_generator.api.words_from_song import random_words_from_song_generator
from password_generator.database.database import db_session, init_db
from password_generator.api.random_characters_generator import random_generator
from password_generator.api.random_words_generator import random_words_generator
from password_generator.scheduler.scheduler import init_scheduler

app = Flask(__name__)
CORS(app, send_wildcard=True)
Swagger(app)

app.register_blueprint(random_generator, url_prefix='api/random/')
app.register_blueprint(random_words_generator, url_prefix='api/random/')
app.register_blueprint(random_words_from_song_generator, url_prefix='api/random')
app.register_blueprint(test_module, url_prefix='api/test')


def main():
    print("Started")
    init_db()
    print("DB started")
    init_scheduler()
    print("Scheduler started")
    app.run(port=8080, host='0.0.0.0')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    main()
