
class MyObject:

    def __init__(self, **kwargs):
        self._set_attrs(kwargs) if kwargs else None

    def _set_attrs(self, d: dict):
        for x, y in d.items():
            setattr(self, x, self.__class__.from_dict(self, y) if isinstance(y, dict) else y)
        return self

    def from_dict(self, d: dict):
        return self._set_attrs(d)

    def clear(self):
        self.__dict__.clear()

    def __str__(self):
        return f'{self.__class__.__name__}<{self.__dict__}>'


if __name__ == '__main__':
    data = {'a': 5, 'b': 7, 'c': {'c1': 9}, "d": {"d1": list(range(10))}}

    ob = MyObject(**data)
    print(ob.d.d1)
