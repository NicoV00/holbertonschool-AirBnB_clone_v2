#!/usr/bin/python3
"""Starts flask 1"""
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


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
