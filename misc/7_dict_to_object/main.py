
class MyObject:

    def set(self, d: dict) -> "MyObject":
        for k, v in d.items():
            setattr(self, k, self.__class__().set(v) if isinstance(v, dict) else v)
        return self

    def clear(self):
        self.__dict__.clear()

    def to_dict(self) -> dict:
        res = {}
        for k, v in self.__dict__.items():
            res[k] = self.__class__.to_dict(v) if isinstance(v, self.__class__) else v
        return res

    def __str__(self):
        return f'{self.__class__.__name__}<{self.__dict__}>'


if __name__ == '__main__':
    data = {'a': 5, 'b': 7, 'c': {'c1': 9}, "d": {"d1": list(range(10))}}

    ob = MyObject()
    ob.set(data)
    print(ob)
    print(ob.to_dict())

    assert ob is not ob.d
