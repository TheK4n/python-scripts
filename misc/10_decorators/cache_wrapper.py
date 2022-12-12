import functools
from timeit import timeit


cached_results = {}


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cached_results
        sorted_arguments_with_func_name = (func.__name__, tuple(sorted(args + tuple(kwargs.values()))))

        if sorted_arguments_with_func_name in cached_results:
            return cached_results[sorted_arguments_with_func_name]
        else:
            res = func(*args, **kwargs)
            cached_results[sorted_arguments_with_func_name] = res
            return res
    return wrapper


@cache
def test(a: float) -> float:
    for _ in range(100_000):
        for _ in range(1_000):
            a += 3.14
    return a


@cache
def test2(a: int) -> int:
    for _ in range(100_000):
        for _ in range(1_000):
            a += 3
    return a



print(timeit("test(1)", number=1, globals=globals()))
print(timeit("test(1)", number=1, globals=globals()))

print(timeit("test2(1)", number=1, globals=globals()))
print(timeit("test2(1)", number=1, globals=globals()))
