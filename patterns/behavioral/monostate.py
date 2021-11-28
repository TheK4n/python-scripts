

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    b1 = Borg()
    b2 = Borg()

    b1.dict = {"a": 1, "b": 2}
    assert b1.dict is b2.dict
    assert b1 is not b2
