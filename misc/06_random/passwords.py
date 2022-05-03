##!/usr/bin/env python3.10
import string
from random import choice

all_chars = [string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
total = "".join(all_chars)


class Password(str):

    def get_power(self) -> int:
        """ Power of password """
        if len(self) < 8:
            return 0

        count = 0
        for symbols in all_chars:
            if any(i in symbols for i in self):
                count += 1
        return count


def get_random_password(length: int, chars: str) -> str:
    chars = Password(chars)
    chars_power = chars.get_power()

    if length < chars_power or length < 8:
        raise ValueError

    password = Password("".join([choice(chars) for _ in range(length)]))
    return password if password.get_power() == chars_power else get_random_password(length, chars)


if __name__ == '__main__':
    print(get_random_password(16, total))
    print(get_random_password(8, string.ascii_lowercase))
    print(get_random_password(8, string.ascii_uppercase + string.ascii_lowercase))
