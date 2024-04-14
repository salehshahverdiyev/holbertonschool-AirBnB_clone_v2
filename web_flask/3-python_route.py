#!/usr/bin/python3
"""
Script Documentation
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
