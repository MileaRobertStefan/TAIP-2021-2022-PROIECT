from flask import Flask, render_template
from flask import request, Response
import json

from backend.obfuscator import Obfuscastor


app = Flask("PROIECT TAIP")


@app.route("/obfuscate-picture")
def obfuscate_page():
    return render_template('HTML/template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


# @app.route("/")
# def obfuscate_page():
#     return render_template('HTML/template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


@app.route("/deobuscate-picture")
def deobfuscate_page():
    return f"<> Salut frate de click <a href=\"https://www.youtube.com/watch?v=8_66C4EyhRQ\">link aici</a> : "


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
