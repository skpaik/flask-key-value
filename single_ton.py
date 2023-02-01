import collections.abc


class SingletonBase(object):
    _instances = {}
    local_map = {}
    local_map_series = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(SingletonBase, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

    def update_dict(self, d, u):
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = self.update_dict(d.get(k, {}), v)
            else:
                d[k] = v
        return d


class Singleton(SingletonBase):
    def put(self, key, value):
        self.local_map[key] = value

    def get(self, key):
        value = ''
        if key in self.local_map:
            value = self.local_map.get(key)

        return value

    def delete(self, key):
        return self.local_map.pop(key, None)

    def put_series1(self, key1, value):
        self.local_map_series.update({key1: value})

    def put_series2(self, key1, key2, value):
        prep_data = {
            key1: {
                key2: value
            }
        }
        self.update_dict(self.local_map_series, prep_data)

    def put_series2_old(self, key1, key2, value):
        key1_value = {}

        if key1 in self.local_map_series:
            key1_value = self.local_map_series.get(key1)

            if not isinstance(key1_value, dict):
                self.local_map_series[key1] = {}
        else:
            self.local_map_series[key1] = {}

        if key2 in key1_value:
            key2_value = key1_value.get(key2)
            if isinstance(key2_value, dict):
                self.local_map_series[key1].update({key2: value})
            else:
                self.local_map_series[key1][key2] = value
        else:
            self.local_map_series[key1].update({key2: value})

        # self.local_map_series[key1][key2] = value

    def put_series3(self, key1, key2, key3, value):
        key3_values_length = 0
        key3_value = self.get_series3(key1, key2, key3)
        if key3_value:
            key3_values_length = len(key3_value)

        prep_data = {
            key1: {
                key2: {
                    key3: {'r' + str(key3_values_length): value}
                }
            }
        }
        self.update_dict(self.local_map_series, prep_data)

    def get_series1(self, key1):
        return self.local_map_series.get(key1, {})

    def get_series2(self, key1, key2):
        value = self.local_map_series.get(key1, {}).get(key2, {})
        return value

    def get_series3(self, key1, key2, key3):
        value = self.local_map_series.get(key1, {}).get(key2, {}).get(key3, {})
        return value

    def delete_series1(self, key1):
        return self.local_map_series.pop(key1, None)
