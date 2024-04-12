#!/usr/bin/python3
"""Starts flask 6"""
from flask import Flask, abort, render_template

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


@app.route('/python/')
@app.route('/python/<text>')
def ptext(text='is cool'):
    """python text"""
    return 'Python {}'.format(text.replace("_", ' '))


@app.route('/number/<n>')
def isanum(n):
    """number int"""
    try:
        return str(n) + ' is a number'
    except ValueError:
        abort(404)


@app.route('/number_template/<n>')
def tmper(n):
    """template display"""
    try:
        return render_template('5-number.html', n=int(n))
    except ValueError:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def evenoroddt(n):
    """ever or odd display"""
    try:
        return render_template('6-number_odd_or_even.html', n=int(n))
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
