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


def set_series_kv(v, k1, k2=None, k3=None):
    url_builder = str(k1)

    if k2:
        url_builder = url_builder + '/' + str(k2)
    if k3:
        url_builder = url_builder + '/' + str(k3)

    r = requests.get(base_url + 'put-series/' + url_builder + '/' + str(v))
    return r.text


def get_series_kv(k1, k2=None, k3=None):
    url_builder = str(k1)

    if k2:
        url_builder = url_builder + '/' + str(k2)
    if k3:
        url_builder = url_builder + '/' + str(k3)

    r = requests.get(base_url + 'get-series/' + url_builder)
    return r.text


def delete_series_kv(k1, k2=None, k3=None):
    url_builder = str(k1)

    if k2:
        url_builder = url_builder + '/' + str(k2)
    if k3:
        url_builder = url_builder + '/' + str(k3)

    r = requests.get(base_url + 'delete-series/' + url_builder)
    return r.text
