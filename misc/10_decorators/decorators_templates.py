from functools import wraps



def func_decorator(name: str):
    """Decorator with arguments"""
    def func_decorator_real(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return func_decorator_real


class FuncDecorator:
    """Decorator-class"""
    def __init__(self, name: str):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper


class ClassDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        self.cls.asdf = 1234
        return self.cls


@ClassDecorator
class Test:
    asdf2 = 321
    pass


a = Test()

# print(a.asdf)
# print(a.asdf2)


# @FuncDecorator("saasd")
@func_decorator("asdf")
def test(a: int):
    """Add one to a"""
    return a + 1



print("DocString:", test.__doc__)
print("FuncName:", test.__name__)
# print(type(test))


