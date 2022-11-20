import requests

base_url = 'http://127.0.0.1:5000/'


def set_kv(k, v):
    r = requests.get(base_url + 'put/' + str(k) + '/' + str(v))
    return r.text


def get_kv(k):
    r = requests.get(base_url + 'get/' + str(k))
    return r.text


def delete_kv(k):
    r = requests.get(base_url + 'delete/' + str(k))
    return r.text
