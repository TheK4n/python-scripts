import time
import hashlib
from simple_random import Random


class TOTP:
    CODE_LIFETIME = 30

    def __init__(self, secret_key: int | None = None):
        if secret_key is None:
            self.__secret_key = self.generete_secret_key()
        else:
            self.__secret_key = secret_key

    def generete_secret_key(self) -> int:
        return read_urandom()

    def get_rest_of_code_lifetime(self) -> int:
        current_time = int(time.time())
        return self.CODE_LIFETIME + current_time - (current_time % self.CODE_LIFETIME) - current_time

    def verify_onetime_code(self, code: int) -> bool:
        return self.generate_onetime_code() == code

    def generate_onetime_code(self) -> int:
        current_time = int(time.time())

        period = current_time - current_time % self.CODE_LIFETIME
        seed = int(f"{self.__secret_key}{period}")

        random = Random(seed)
        res = random.randint()
        return res

    def get_secret_key(self) -> int:
        return self.__secret_key


def read_urandom(chunk: int = 4096) -> int:
    return int(hashlib.sha256(open("/dev/urandom", "rb").read(chunk)).hexdigest(), base=16)

