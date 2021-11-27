from threading import Lock, Thread


class Database:
    __lock: Lock = Lock()

    __instance = None
    is_connected = False

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance

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


def test(user, passwd, port):
    db = Database(user, passwd, port)
    print(db.user)


if __name__ == '__main__':
    process1 = Thread(target=test, args=('root', 'toor', 1101))
    process2 = Thread(target=test, args=('user', '1234', 5221))
    process1.start()
    process2.start()
