
class MyObject:

    def set_attrs(self, d: dict):
        for x, y in d.items():
            setattr(self, x, self.__class__().set_attrs(y) if isinstance(y, dict) else y)

    def clear(self):
        self.__dict__.clear()

    def __str__(self):
        return f'{self.__class__.__name__}<{self.__dict__}>'


if __name__ == '__main__':
    data = {'a': 5, 'b': 7, 'c': {'c1': 9}, "d": {"d1": list(range(10))}}

    ob = MyObject()
    ob.set_attrs(data)
    print(ob.d.d1)

    assert ob is not ob.d
