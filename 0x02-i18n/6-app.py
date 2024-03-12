#!/usr/bin/env python
"""Task 6 Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)


class Config:
    """flask Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """retrieves user"""
    try:
        user_id = request.args.get('login_as', '')
        return users.get(int(user_id), None)
    except Exception:
        return

@app.before_request
def before_request() -> None:
    """gets argument"""
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    """gets the locale for the webpage"""
    requested_locale = request.args.get('locale', '')
    if requested_locale in app.config["LANGUAGES"]:
        return requested_locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
