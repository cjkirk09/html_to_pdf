from flask import Flask, render_template

# url_for('static', filename='style.css')
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)
