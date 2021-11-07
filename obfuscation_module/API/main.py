from flask import Flask, render_template
from flask import request, Response
import json

from backend.obfuscator import Obfuscastor


app = Flask("PROIECT TAIP")

@app.route("/obfuscate", methods=["GET", "POST"])
def obfuscate():
    if request.method == "GET":
        return " GET "

    if request.method == "POST":
        photos = request.files['photo']
        zones = json.loads(request.form['zones'])
        res = Response(Obfuscastor.post(photos, zones), mimetype='json/txt')

    return res


@app.route("/deobfuscate")
def deobfuscate():
    return "<p>Hello, World!</p>"


print("Merge frate!")
app.run()
