
def constrain(val, range_min, range_max):
    """
    Constrains range
    """
    if val < range_min:
        return range_min
    elif val > range_max:
        return range_max
    else:
        return val


def map(val, old_min, old_max, new_min, new_max):
    """
    Converts range
    """
    old_range = old_max - old_min
    if old_range == 0:
        return new_max
    else:
        new_range = new_max - new_min
        return (((val - old_min) * new_range) / old_range) + new_min
