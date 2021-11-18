import main


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


def convert(val, old_min, old_max, new_min, new_max):
    """
    Converts range
    """
    old_range = old_max - old_min
    if old_range == 0:
        return new_max
    else:
        new_range = new_max - new_min
        return (((val - old_min) * new_range) / old_range) + new_min


def triangulator(a, b, delta_dist=25):
    a = (a + 360) % 360
    b = (b + 360) % 360

    if a < b:
        delta = abs(360 + a - b)
    else:
        delta = abs(b - a)
    return round(delta_dist / math.sin(math.radians(delta)), 2)