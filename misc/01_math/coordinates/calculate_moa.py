import math


MOA_PER_CLICK = 0.25
DISTANCE = 275  # meters
DEVITATION = 40 # centimeter


def calculate_moa(distance: float, devitation: float) -> float:
    hypo = math.sqrt(pow(devitation, 2) + pow(distance, 2))
    return math.degrees(math.asin(devitation / hypo)) * 60


def calculate_devitation(distance: float, moa: float) -> float:
    return math.tan(math.radians(moa/60)) * distance


if __name__ == "__main__":
    print("Distance:", DISTANCE, "meters")
    print("Clicks:", round(calculate_moa(DISTANCE, DEVITATION / 100) / MOA_PER_CLICK, 3), "by", DEVITATION, "centimeters")
    print("Devitation by 1 click:", round(calculate_devitation(DISTANCE, 1 * MOA_PER_CLICK) * 100, 3), "centimeters")

