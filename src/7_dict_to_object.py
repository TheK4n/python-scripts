class MyObject:

    def _set_attrs(self, d: dict):
        for x, y in d.items():
            setattr(self, x, MyObject.from_dict(self, y) if isinstance(y, dict) else y)
        return self

    def from_dict(self, d):
        return self._set_attrs(d)

    def from_params(self, **kwargs):
        return self._set_attrs(kwargs)


if __name__ == '__main__':

    data1 = {'a': 5, 'b': 7, 'c': {'d': 8}}
    data2 = {'a': 5, 'b': 7, 'c': {'d': 9}, "new": {"some_list": list(range(10))}}

    ob = MyObject()
    ob.from_dict(data1)
    print(ob.c.d)

    ob2 = MyObject()
    ob2.from_params(**data2)
    print(ob2.new.some_list)
