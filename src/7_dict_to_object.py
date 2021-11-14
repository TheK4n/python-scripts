class MyObject:

    def from_dict(self, d):
        for x, y in d.items():
            setattr(self, x, MyObject.from_dict(self, y) if isinstance(y, dict) else y)
        return self

    def from_params(self, **kwargs):
        for x, y in kwargs.items():
            setattr(self, x, MyObject.from_dict(self, y) if isinstance(y, dict) else y)
        return self


if __name__ == '__main__':

    data = {'a': 5, 'b': 7, 'c': {'d': 8}}

    ob = MyObject()
    ob.from_dict(data)
    print(ob.c.d)

    ob2 = MyObject()
    ob2.from_params(**data)
    print(ob2.c.d)
