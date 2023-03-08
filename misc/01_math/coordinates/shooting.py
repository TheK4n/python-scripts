#!/usr/bin/env python3
import math


ONE_MOA_IN_MILS = 0.2909
ONE_MIL_IN_MOA = 3.43


def calculate_moa(distance: float | int, devitation: float | int) -> float:
    """
    distance in meters
    devitation in centimeters
    """
    hypo = math.sqrt(pow(devitation, 2) + pow(distance, 2))
    return math.degrees(math.asin(devitation / hypo)) * 60


def calculate_devitation(distance: float | int, moa: float | int) -> float:
    """
    distance in meters
    """
    return math.tan(math.radians(moa/60)) * distance


def calculate_distance_from_target_size_and_mils(size: float | int, mils: float | int) -> float:
    """
    size in meters
    """
    return (size * 1000) / mils


def convert_moa_to_mils(moa: float | int) -> float:
    return moa * ONE_MOA_IN_MILS


def convert_mils_to_moa(mils: float | int) -> float:
    return mils * ONE_MIL_IN_MOA


if __name__ == "__main__":
    moa_per_click = 0.25
    distance = 275  # meters
    devitation = 40 # centimeter
    print("Distance:", distance, "meters")
    print("Clicks:", round(calculate_moa(distance, devitation / 100) / moa_per_click, 3), "by", devitation, "centimeters")
    print("Devitation by 1 click:", round(calculate_devitation(distance, 1 * moa_per_click) * 100, 3), "centimeters")

