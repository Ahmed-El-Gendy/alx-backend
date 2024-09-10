#!/usr/bin/env python3
"""
Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get user or None
    """
    login_id = request.args.get('login_as')
    if login_id:
        user = users.get(int(login_id))
    else:
        user = None
    return user


@app.before_request
def before_request():
    """
    Before request method
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locate = request.args.get('locale')
    if locate in app.config['LANGUAGES']:
        return locate
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Default route
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
