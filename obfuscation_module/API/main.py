import json

from flask import Flask
from flask import Response

from backend.obfuscator import Obfuscastor

app = Flask("PROIECT TAIP")

from flask import Flask, render_template, make_response, send_from_directory, request

app = Flask(__name__)


@app.route("/obfuscate-page")
def template_test():
    return render_template('smart-select-image.html', my_string="Wheeeee!")


@app.route("/deobfuscate-page")
def deobfuscate_page():
    image_name = request.args.get('image-name')
    if image_name != None:
        return render_template('view-obfuscated-image.html', img_name=image_name)
    else:
        return None


@app.route('/style.css')
def css():
    resp = make_response(render_template("css/custom.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp


@app.route('/custom.js')
def js():
    resp = make_response(render_template("js/custom.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory('backend/images', path)


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
