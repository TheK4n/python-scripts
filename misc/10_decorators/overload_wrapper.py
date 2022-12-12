
KEYS = {}


def overload(func):
    global KEYS

    types = tuple(func.__annotations__.values())
    func_key = (func.__name__, types)
    KEYS[func_key] = func

    def inner(*args, **kwargs):
        global KEYS

        arguments = args + tuple(kwargs.values())
        types = tuple(map(type, arguments))
        func_key = (inner.__name__, types)

        saved_func = KEYS[func_key]
        res = saved_func(*args, **kwargs)

        return res
    inner.__name__ = func.__name__

    return inner


@overload
def append(a: str, b: str):
    return a + b


@overload
def append(a: int, b: int):
    return a / b


@overload
def append(a: str, b: int):
    return a * b


@overload
def some(a: int, b: int):
    return a + b


assert append("huy", 2) == "huyhuy"
assert append("da", "net") == "danet"
assert append(24, 2) == 12
assert append("da ", 3) == "da da da "

