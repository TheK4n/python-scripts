import time


class Random:

    def __init__(self, seed: int | None = None):
        self.__set_seed(seed)

    def set_seed(self, seed: int | None = None):
        self.__set_seed(seed)

    def __set_seed(self, seed: int | None = None):
        if seed is None:
            self.__seed = int(time.time())
        else:
            self.__seed = seed

    def randint(self, end: int = 0xFFFF) -> int:
        self.__seed = (self.__seed * 73129 + 95121) % end
        return self.__seed

