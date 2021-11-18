from main import time
import random


class Timer:
    def __init__(self):
        self.__start_time = time()

    def duration(self):
        return time() - self.__start_time


if __name__ == '__main__':

    timer = Timer()

    lst = [random.randint(1, 888898) for num in range(1, 1000000) if num % 2 == 0]

    print(f'Elapsed {timer.duration()} sec')
