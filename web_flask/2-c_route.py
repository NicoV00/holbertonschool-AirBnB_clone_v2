#!/usr/bin/python3
"""Starts flask 3"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """prints hello"""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """prints hbnb"""
    return "HBNB"

@app.route('/c/<text>')
def ctext(text):
    """prints c text"""
    return 'C ' + text.replace("_", ' ')


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
