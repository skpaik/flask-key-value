from fkv_helper import set_kv, get_kv, delete_kv, set_series_kv, get_series_kv, delete_series_kv

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

send_time = {
    'fs': {
        'h2': 37.99,
        'h3': 41.889
    },
    'ed': {
        'h2': 56.444,
        'h3': 77.000
    }
}

dict_data = 78

# r = set_series_kv(dict_data, 'send_time')
# print(r)
#
# r = set_series_kv(46, 'send_time')
# print(r)
# r = set_series_kv(46, 'send_time', 'fs')
# print(r)
# r = set_series_kv(74, 'send_time', 'ed')
# print(r)

r = set_series_kv('37.99', 'send_time', 'fs', 'h2')
print(r)

r = set_series_kv('41.889', 'send_time', 'fs', 'h3')
print(r)

r = get_series_kv('send_time')
print(r)
r = get_series_kv('send_time', 'fs')
print(r)
r = get_series_kv('send_time', 'fs', 'h2')
print(r)
r = get_series_kv('send_time', 'fs', 'h3')
print(r)

# r = set_series_kv(dict_data, 'send_time', 'ed')
# print(r)

r = set_series_kv('56.444', 'send_time', 'ed', 'h2')
print(r)

r = set_series_kv('77.000', 'send_time', 'ed', 'h3')
print(r)
r = set_series_kv('78.000', 'send_time', 'ed', 'h3')
print(r)
r = set_series_kv('78.000', 'send_time', 'ed', 'h2')
print(r)
r = set_series_kv('79.000', 'send_time', 'ed', 'h4')
print(r)
r = set_series_kv('80.000', 'send_time', 'ed', 'h4')
print(r)
r = set_series_kv('81.000', 'send_time', 'ed', 'h4')
print(r)
r = set_series_kv('82.000', 'send_time', 'ed', 'h4')
print(r)
r = set_series_kv('83.000', 'send_time', 'ed', 'h4')
print(r)

r = get_series_kv('send_time')
print(r)
r = get_series_kv('send_time', 'ed')
print(r)
r = get_series_kv('send_time', 'fs')
print(r)
r = get_series_kv('send_time', 'ed', 'h2')
print(r)
r = get_series_kv('send_time', 'ed', 'h3')
print(r)
