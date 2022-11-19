class SingletonBase(object):
    _instances = {}
    local_map = {}

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
