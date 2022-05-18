#!/usr/bin/env python3
"""Simple Flask Application"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configuration for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    GET root
    renders 3-index.html
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
