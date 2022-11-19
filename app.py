from flask import Flask
from single_ton import Singleton

app = Flask(__name__)

cd = Singleton()


@app.route("/")
def hello_world():
    s = """ <p>
            <strong>Flask Key Value Pair is running</strong>......</br></br></br>
            You can follow some example in `tests/kv.py` file</br>
            Thanks for using Flask Key Value App</br>
            </p>
            """
    return s


@app.route('/put/<key>/<value>')
@app.route('/put/<key>/<value>/')
def put_key_value(key, value):
    cd.put(key, value)
    print('LOG: PUT', key, value)
    return "ok"


@app.route('/get/<key>')
@app.route('/get/<key>/')
def get_key_value(key):
    value = cd.get(key)
    print('LOG: GET', key, value)
    return value


@app.route('/delete/<key>')
@app.route('/delete/<key>/')
def delete_key_value(key):
    value = cd.delete(key)
    print('LOG: DELETE', key, value)
    return value
