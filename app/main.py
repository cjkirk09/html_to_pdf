from flask import Flask, render_template
from wkhtml import generatePdf as wkhtmlGeneratePdf
from phantom import generatePdf as phantomGeneratePdf

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


@app.route('/wk/<path>')
@app.route('/wk/<path>/')
def wkhtml_pdf(path=None):
    if path:
        path = validatePath(path)
        return wkhtmlGeneratePdf(path)


@app.route('/ph/<path>')
@app.route('/ph/<path>/')
def phantom_pdf(path=None):
    if path:
        path = validatePath(path)
        return phantomGeneratePdf(path)


def validatePath(path):
    path = path.rstrip('/')
    return path
