#!/usr/bin/python3
"""
Script Documentation
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    Method Documentation
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Method Documentation
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Method Documentation
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Method Documentation
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Method Documentation
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Method Documentation
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Method Documentation
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
