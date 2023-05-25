from collections import UserDict
from keyword import iskeyword
from typing import Hashable


class NamedDict(UserDict):

    def __setitem__(self, key: Hashable, item):
        if isinstance(key, str):
            if iskeyword(key) or not key.isidentifier() or key == "data":
                key = "_" + key
            setattr(self, key, self.__class__(item) if isinstance(item, dict) else item)
        super().__setitem__(key, item)

    def update(self, d: dict):
        for k, v in d.items():
            self[k] = v

    def __str__(self):
        return f"{self.__class__.__name__}({self.data})"


if __name__ == '__main__':
    data = {
        'for': 5,
        '1b': 'ni',
        'b': 7,
        'c': {
            'c1': 9
        },
        "d": {
            "d1": [1, 2, 3]
        }
    }

    ob = NamedDict(data)
    print(ob)

    assert ob is not ob.d

