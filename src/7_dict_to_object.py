class MyObject:

    def __init__(self, d: dict = None):
        self._set_attrs(d) if d else None

    def _set_attrs(self, d: dict):
        for x, y in d.items():
            setattr(self, x, self.__class__.from_dict(self, y) if isinstance(y, dict) else y)
        return self

    def from_dict(self, d: dict):
        return self._set_attrs(d)

    def from_params(self, **kwargs):
        return self._set_attrs(kwargs)

    def clear(self):
        self.__dict__.clear()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


if __name__ == '__main__':
    data1 = {'a': 5, 'b': 7, 'c': {'d': 8}}
    data2 = {'a': 5, 'b': 7, 'c': {'d': 9}, "new": {"some_list": list(range(10))}}

    ob = MyObject()
    ob.from_dict(data1)
    print(ob.c.d)

    ob2 = MyObject()
    ob2.from_params(**data2)
    print(ob2.new.some_list)
    print(ob2)
