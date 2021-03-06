from main import MyObject


class MyObjectMonostate(MyObject):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def to_dict(self):
        res = {}
        for k, v in self.__dict__.items():
            res[k] = v
        return res


if __name__ == '__main__':
    b1 = MyObjectMonostate()
    b1.set({"a": [1, 2, 3], "b": {"b1": 1}})
    b2 = MyObjectMonostate()
    print(b2.to_dict())

    assert b1.a is b2.a  # is monostate working
    assert b1 is not b2  # are different instances

    assert b1 is not b1.b  # is internal instance is different from external
    assert b1.__dict__ is b1.b.__dict__  # is internal instance is monostate with external
