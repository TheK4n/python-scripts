import copy


class Prototype:
    """
    Copy object
    """
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name):
        obj = copy.deepcopy(self._objects[name])
        return obj


class Test:
    a = 2
    b = 3

    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    t = Test(123)
    t.a = 1

    prototype = Prototype()
    prototype.register("Test", t)
    t2 = prototype.clone("Test")

    print(t2.x)
