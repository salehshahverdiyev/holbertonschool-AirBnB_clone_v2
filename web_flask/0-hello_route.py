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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
