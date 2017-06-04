from flask import Flask, render_template, request
from wkhtml import generatePdf as wkhtmlGeneratePdf
from phantom import generatePdf as phantomGeneratePdf
from hobbit_text import hobbit_text

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
@app.route('/hello/', methods=['GET'])
@app.route('/hello/<name>', methods=['GET'])
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/populated_with_js/', methods=['GET'])
def populated_with_js():
    return render_template('populated_with_js.html')


@app.route('/hobbit-text', methods=['GET'])
def get_hobbit_text():
    return hobbit_text


@app.route('/wk/')  # index page
@app.route('/wk/<path>')
@app.route('/wk/<path>/')
def wkhtml_pdf(path=''):
    path = validatePath(path)
    no_smart_shrinking = request.args.get('nss', '') == 't'
    return wkhtmlGeneratePdf(path, no_smart_shrinking=no_smart_shrinking)


@app.route('/ph/')  # index page
@app.route('/ph/<path>')
@app.route('/ph/<path>/')
def phantom_pdf(path=''):
    path = validatePath(path)
    return phantomGeneratePdf(path)


def validatePath(path):
    path = path.rstrip('/')
    return path
