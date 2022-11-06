import requests

base_url = 'http://127.0.0.1:5000'
r = requests.get(base_url + '/put/a/291')
print(r.text)
r = requests.get(base_url + '/put/b/420')
print(r.text)
r = requests.get(base_url + '/get/b')
print(r.text)

dict_data = {
    "action": 196,
    'route': 475,
    'switch': 3333
}

r = requests.get(base_url + '/put/d/' + str(dict_data))
print(r.text)
r = requests.get(base_url + '/get/d')
print(r.text)
