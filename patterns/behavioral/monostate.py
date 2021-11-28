

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    b1 = Borg()
    b2 = Borg()

    b1.a = {"a": 1, "b": 2}
    assert b1.a is b2.a

