
cached_results = {}


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cached_results
        sorted_arguments = tuple(set(args + tuple(kwargs.values())))

        if sorted_arguments in cached_results:
            return cached_results[sorted_arguments]
        else:
            res = func(*args, **kwargs)
            cached_results[sorted_arguments] = res
            return res
    return wrapper
