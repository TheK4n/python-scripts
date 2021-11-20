from src.alphabet import *

__all__ = ["encode", "decode"]


def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}


def encode(text: str, alphabet: dict = eng) -> str:
    res = ""
    for i in text.lower():
        res += (alphabet[i] if i in alphabet else i) + " "
    return res


def decode(text: str, alphabet: dict = eng) -> str:

    alphabet = reverse_dict(alphabet)

    res = []
    for i in text.lower().split(' '):
        if i == '':
            res += ' '
        else:
            res.append(alphabet[i] if i in alphabet else i)
    return "".join(res).replace("  ", " ").strip()


if __name__ == '__main__':
    encoded_text = encode("сос сос сос", alphabet=rus)
    print(encoded_text)
    print(decode(encoded_text, alphabet=rus))
