#!/usr/bin/python3
"""hello_route"""
from flask import Flask

app = Flask(__name__)


@app.route("/",  strict_slashes=False)
def hello_hbnb():
    """This route returns a "Hello HBNB!" string"""
    return "Hello HBNB!"


@app.route("/hbnb",  strict_slashes=False)
def hbnb_route():
    """This route returns a "HBNB" string"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
