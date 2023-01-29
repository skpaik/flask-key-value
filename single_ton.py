class SingletonBase(object):
    _instances = {}
    local_map = {}
    local_map_series = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(SingletonBase, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


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
        self.local_map_series[key1] = value

    def put_series2(self, key1, key2, value):
        if key1 in self.local_map_series:
            key1_value = self.local_map_series.get(key1)
            if not isinstance(key1_value, dict):
                self.local_map_series[key1] = {}
        else:
            self.local_map_series[key1] = {}

        self.local_map_series[key1][key2] = value

    def put_series3(self, key1, key2, key3, value):
        self.put_series2(key1, key2, {})

        self.local_map_series[key1][key2][key3] = value

    def get_series1(self, key1):
        return self.local_map_series.get(key1, '')

    def get_series2(self, key1, key2):
        value = self.local_map_series.get(key1, {})
        if not isinstance(value, dict):
            return ''

        return value.get(key2, '')

    def get_series3(self, key1, key2, key3):
        value = self.local_map_series.get(key1, {})
        if not isinstance(value, dict):
            return ''

        value = value.get(key2, '')
        if not isinstance(value, dict):
            return ''

        return value.get(key3, '')

    def delete_series1(self, key1):
        return self.local_map_series.pop(key1, None)
