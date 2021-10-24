from flask import Flask

app = Flask(__name__)


@app.route("/obfuscate")
def obfuscate():
    return "<p>Hello, World!</p>"


@app.route("/deobfuscate")
def deobfuscate():
    return "<p>Hello, World!</p>"
