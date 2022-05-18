#!/usr/bin/env python3
"""Simple Flask Application"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, exceptions

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    gets user from url parameter, if nothing
    is passed or user not in users, returns None
    """
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as))
        if user:
            return user
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


class Config(object):
    """configuration for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('7-app.Config')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """infer appropiate timezone"""
    tz = request.args.get('timezone')
    if tz:
        try:
            return timezone(tz).zone
        except exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    GET root
    renders 7-index.html
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
