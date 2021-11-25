class Database:
    __instance = None
    is_connected = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)

    def __init__(self, user: str, passwd: str, port: int):

        # if any attribute is not defined
        if not all(map(lambda attr: hasattr(self, attr), ("user", "passwd", "port"))):
            self.user = user
            self.passwd = passwd
            self.port = port

    def __del__(self):
        self.__instance = None
        self.close()

    def connect(self):

        if self.is_connected:
            raise Exception("Already connected")

        print(f"Connect to db://{self.user}@{self.passwd}:{self.port}")
        self.is_connected = True

    def close(self):
        self.is_connected = False


if __name__ == '__main__':
    db = Database('root', 'toor', 1101)
    db2 = Database('user', '1234', 5221)
    assert db is db2
