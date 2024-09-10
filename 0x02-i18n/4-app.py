#!/usr/bin/env python3
"""
Babel setup
"""
from flask import Flask, render_template, request
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


@babel.localselector
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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
