from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('smart-select-image.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


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


@app.route("/obfuscate")
def obfuscate():
    return "<p>Hello, World!</p>"


@app.route("/deobfuscate")
def deobfuscate():
    return "<p>Hello, World!</p>"
