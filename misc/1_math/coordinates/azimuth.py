def phi2az(val: int | float) -> int:
    """
    -180:180 -> 0, 360
    """

    if val not in range(-180, 181):
        raise ValueError(f"{val} if out of range")

    val = round(val)

    if val <= 90:
        return 90 - val
    elif 90 <= val < 180:  # between 90 and 180
        return 360 - (val - 90)
    else:
        return val + 90


def get_direction(azimuth: int) -> str:
    """Returns direction from azimuth"""

    if azimuth in range(0, 24):
        return 'north'
    elif azimuth in range(338, 361):
        return 'north'
    elif azimuth in range(24, 76):
        return 'north-east'
    elif azimuth in range(76, 113):
        return 'east'
    elif azimuth in range(113, 158):
        return 'south-east'
    elif azimuth in range(158, 203):
        return 'south'
    elif azimuth in range(203, 248):
        return 'south-west'
    elif azimuth in range(248, 292):
        return'west'
    elif azimuth in range(292, 338):
        return 'north-west'
    else:
        raise ValueError(f"{azimuth} if out of range")


def az2clock(azimuth: int) -> int:
    """
    0:369 -> 1:12
    """
    return azimuth * 12 // 360 if azimuth else 12


def clock2az(clock: int) -> int:
    """
    1:12 -> 0:359
    """
    if clock == 12:
        return 0

    return clock * 360 // 12
