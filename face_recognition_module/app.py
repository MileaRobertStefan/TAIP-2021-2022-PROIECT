
from flask import Flask

app = Flask(__name__)


@app.route("/detection")
def detection():
    return "<p>Hello, World!</p>"


@app.route("/recognition")
def recognition():
    return "<p>Hello, World!</p>"