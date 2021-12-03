
class MyObject:
    __shared_state = {}

    def __init__(self, **kwargs):
        self.__dict__ = self.__shared_state
        self._set_attrs(kwargs) if kwargs else None

    def _set_attrs(self, d: dict):
        for x, y in d.items():
            setattr(self, x, self.__class__()._set_attrs(y) if isinstance(y, dict) else y)
        return self

    def clear(self):
        self.__shared_state.clear()

    def __str__(self):
        return f'{self.__class__.__name__}<{self.__shared_state}>'


if __name__ == '__main__':
    b1 = MyObject(**{"a": [1, 2, 3], "b": {"b1": 1}})
    b2 = MyObject()

    assert b1.a is b2.a
    assert b1 is not b2

    assert b1 is not b1.b
