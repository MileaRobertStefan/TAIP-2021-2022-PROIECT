import json

from flask import Flask, Response

from backend.deobfuscator import Deobfuscator
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

    if image_name:
        s = "src=/images/" + image_name + ""
        t = render_template('view-obfuscated-image.html', img_name=s)
    else:
        t = render_template('view-obfuscated-image.html', img_name="")

    return t


@app.route('/style.css')
def css():
    resp = make_response(render_template("css/custom.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp


@app.route('/index.js')
def js():
    resp = make_response(render_template("js/index.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/rectangles_drawer')
def js_drawer():
    resp = make_response(render_template("js/rectangles_drawer.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/rectangle_drawer_utils')
def js_drawer_utils():
    resp = make_response(render_template("js/rectangle_drawer_utils.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/faces_detector')
def js_faces_detector():
    resp = make_response(render_template("js/faces_detector.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/obfuscation_utils')
def js_obfuscation_utils():
    resp = make_response(render_template("js/obfuscation_utils.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/deobfuscation_utils')
def js_deobfuscation_utils():
    resp = make_response(render_template("js/deobfuscation_utils.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/export_utils')
def js_export_utils():
    resp = make_response(render_template("js/export_utils.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp


@app.route('/FileSaver.js')
def FileSaver():
    resp = make_response(render_template("js/FileSaver.js"))
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


@app.route("/deobfuscate", methods=["GET", "POST"])
def deobfuscate():
    if request.method == "POST":
        image_id = request.form["image_id"]
        zones = request.form["zones"]

        img = Deobfuscator.post(image_id, zones)

        response = make_response(img)
        return response

    if request.method == "GET":
        image_id = request.form["image_id"]
        zones = request.form["zones"]

        img = Deobfuscator.post(image_id, zones)

        response = make_response(img.tobytes())
        return response

    return "<p>Hello, World!</p>"


print("http://127.0.0.1:5000/obfuscate-page")
app.run(debug=True)
