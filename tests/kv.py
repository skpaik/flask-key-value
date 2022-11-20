from fkv_helper import set_kv, get_kv, delete_kv

r = set_kv('a', 291)
print(r)

r = set_kv('b', 420)
print(r)

r = get_kv('b')
print(r)

dict_data = {
    "action": 196,
    'route': 475,
    'switch': 3333
}

r = set_kv('d', dict_data)
print(r)
r = get_kv('d')
print(r)

r = delete_kv('d')
print(r)
