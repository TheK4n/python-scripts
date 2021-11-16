def expand_key(text: str, key: str):
    while True:
        if len(text) == len(key):
            return key
        elif len(key) > len(text):
            return key[:len(text)]
        elif len(key) < len(text):
            key *= 2


def enc_caesar(msg: str, shift: int, alphabet: str) -> str:
    alphabet = tuple(alphabet)

    ret = ""
    for x in msg:
        if x in alphabet:
            ind = alphabet.index(x) % len(alphabet)
            ret += alphabet[(ind + shift) % len(alphabet)]
        else:
            ret += x
    return ret


def dec_caesar(msg: str, shift: int, alphabet: str):
    alphabet = tuple(alphabet)

    ret = ""

    for x in msg:

        if x in alphabet:
            ind = alphabet.index(x)
            ret += alphabet[ind - shift]
        else:
            ret += x
    return ret


def crypt_atbash(msg: str, alphabet: str) -> str:
    alphabet = tuple(alphabet)
    ret1 = ''

    for x in msg:

        if x in alphabet:
            ind = alphabet.index(x) % len(alphabet)
            alphabet = alphabet[::-1]
            ret = alphabet[ind]
            ret1 += ret
        else:
            ret1 += x

    return ret1


def enc_vigener(msg: str, key: str, alphabet: str, *, shift: int = 0):

    key = expand_key(msg, key)

    alphabet = tuple(alphabet)
    ret = ''
    space = 0
    for index, ch in enumerate(msg):
        if ch in alphabet:
            mj = alphabet.index(ch)
            kj = alphabet.index(key[(index - space) % len(key)].lower())
            cj = (mj + kj + shift) % len(alphabet)
            ret += alphabet[cj]
        else:
            ret += ch
            space += 1
    return ret


def dec_vigener(msg: str, key: str, alphabet: str, *, shift: int = 0):

    key = expand_key(msg, key)

    alphabet = tuple(alphabet)
    ret = ''
    space = 0
    for index, ch in enumerate(msg):
        if ch in alphabet:
            cj = alphabet.index(ch)
            kj = alphabet.index(key[(index - space) % len(key)].lower())
            mj = (cj - kj - shift) % len(alphabet)
            ret += alphabet[mj]
        else:
            ret += ch
            space += 1
    return ret


def enc_test(msg: str):
    return '%'.join([hex(~ord(i)) for i in list(msg)])


def dec_test(msg: str):
    return ''.join([chr(~int(i, 16)) for i in msg.split('%')])


def coding(msg: str, key: int):
    return ''.join([chr(ord(i) ^ key) for i in msg])