from main import NamedDict


class MyObjectMonostate(NamedDict):
    __shared_state = {}

    def __init__(self, dict=None, /, **kwargs):
        self.__dict__ = self.__shared_state
        super().__init__(dict, **kwargs)


if __name__ == '__main__':
    
    b1 = MyObjectMonostate({"a": [1, 2, 3], "b": {"b1": 1}})
    b2 = MyObjectMonostate()


    assert b1.a is b2.a  # is monostate working
    assert b1 is not b2  # are different instances

    assert b1 is not b1.b  # is internal instance is different from external
    assert b1.__dict__ is b1.b.__dict__  # is internal instance is monostate with external
