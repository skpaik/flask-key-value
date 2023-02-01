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


@app.route('/put-series/<key1>/<value>')
@app.route('/put-series/<key1>/<value>/')
def put_key1_series_value(key1, value):
    cd.put_series1(key1, value)
    print('LOG: PUT Series 1', key1, value)
    return "ok"


@app.route('/put-series/<key1>/<key2>/<value>')
@app.route('/put-series/<key1>/<key2>/<value>/')
def put_key2_series_value(key1, key2, value):
    cd.put_series2(key1, key2, value)
    print('LOG: PUT Series 2', key1, key2, value)
    return "ok"


@app.route('/put-series/<key1>/<key2>/<key3>/<value>')
@app.route('/put-series/<key1>/<key2>/<key3>/<value>/')
def put_key3_series_value(key1, key2, key3, value):
    cd.put_series3(key1, key2, key3, value)
    print('LOG: PUT Series 3', key1, key2, key3, value)
    return "ok"


@app.route('/get-series/<key1>')
@app.route('/get-series/<key1>/')
def get_key1_series_value(key1):
    value = cd.get_series1(key1)
    print('LOG: GET Series 1', key1, value)
    return value


@app.route('/get-series/<key1>/<key2>')
@app.route('/get-series/<key1>/<key2>/')
def get_key2_series_value(key1, key2):
    value = cd.get_series2(key1, key2)
    print('LOG: GET Series 2', key1, key2, value)
    return value


@app.route('/get-series/<key1>/<key2>/<key3>')
@app.route('/get-series/<key1>/<key2>/<key3>/')
def get_key3_series_value(key1, key2, key3):
    value = cd.get_series3(key1, key2, key3)
    print('LOG: GET Series 3', key1, key2, key3, value)
    return value


@app.route('/delete-series/<key1>')
@app.route('/delete-series/<key1>/')
def delete_key1_value(key1):
    value = cd.delete_series1(key1)
    print('LOG: DELETE Series 1', key1, value)
    return value
