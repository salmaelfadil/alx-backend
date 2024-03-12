#!/usr/bin/env python
"""Task 2 Module"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """flask Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """gets the locale for the webpage"""
    return request.accept_languages.best_match(["LANGUAGES"])

@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
