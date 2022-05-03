def get_direction(azimuth: int) -> str:
    """Returns direction from azimuth"""

    if azimuth in range(0, 24):
        return 'north'
    if azimuth in range(338, 361):
        return 'north'
    if azimuth in range(24, 76):
        return 'north-east'
    if azimuth in range(76, 113):
        return 'east'
    if azimuth in range(113, 158):
        return 'south-east'
    if azimuth in range(158, 203):
        return 'south'
    if azimuth in range(203, 248):
        return 'south-west'
    if azimuth in range(248, 292):
        return 'west'
    if azimuth in range(292, 338):
        return 'north-west'
    raise ValueError(f"{azimuth} out of range")


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
