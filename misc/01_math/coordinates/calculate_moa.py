import math
import sys


def calculate_moa(distance, devitation):
    hypo = math.sqrt(pow(devitation, 2) + pow(distance, 2))
    return math.degrees(math.asin(devitation / hypo)) * 60


if __name__ == "__main__":
    print(calculate_moa(*map(float, sys.argv[1:3])))

