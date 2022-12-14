from typing import Callable


__OVERLOADED_FUNCTIONS: dict[tuple[str, tuple[type]], Callable] = {}


def overload(func):
    annotations = func.__annotations__.copy()
    if "return" in annotations:
        del annotations["return"]

    types = tuple(annotations.values())
    func_name = f"{func.__module__}.{func.__name__}"
    key = (func_name, types)
    __OVERLOADED_FUNCTIONS[key] = func

    def inner(*args, **kwargs):
        arguments = args + tuple(kwargs.values())
        types = tuple(map(type, arguments))
        func_name = f"{func.__module__}.{func.__name__}"
        key = (func_name, types)

        saved_func = __OVERLOADED_FUNCTIONS[key]
        res = saved_func(*args, **kwargs)

        return res

    inner.__name__ = func.__name__
    return inner


@overload
def some_func(a: str, b: str):
    return a + b


@overload
def some_func(a: int, b: int):
    return a / b


@overload
def some_func(a: str, b: int):
    return a * b


@overload
def some(a: int, b: int):
    return a + b


assert some_func("La", 2) == "LaLa"
assert some_func("Yes", "No") == "YesNo"
assert some_func(24, 2) == 12
assert some_func("La ", 3) == "La La La "
assert some(5, 3) == 8

print(__OVERLOADED_FUNCTIONS)

