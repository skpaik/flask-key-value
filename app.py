from flask import Flask
from single_ton import Singleton

app = Flask(__name__)

cd = Singleton()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello')
def hello():
    return 'Hello, World2 '


@app.route('/put/<key>/<value>')
@app.route('/put/<key>/<value>/')
def put_key_value(key, value):
    cd.put(key, value)
    return "ok"


@app.route('/get/<key>')
@app.route('/get/<key>/')
def get_key_value(key):
    return cd.get(key)
