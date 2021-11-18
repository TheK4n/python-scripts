import requests
from datetime import datetime
from random import random


def get_random_list(num: int, min_: int, max_: int) -> list[int]:
    url = f'http://www.random.org/integers/?num={num}&min={min_}&max={max_}&col=1&format=plain&rnd=new&base=10'

    resp = requests.get(url)

    return list(map(int, resp.text.strip().split('\n')))


def get_shuffled_list(min_: int, max_: int) -> list[int]:
    url = f'http://www.random.org/sequences/?min={min_}&max={max_-1}&col=1&format=plain&rnd=new'

    resp = requests.get(url)

    return list(map(int, resp.text.strip().split('\n')))


def get_random_string(length: int, digits: bool = True, uppercase: bool = True, lowercase: bool = True) -> str:

    url = f'http://www.random.org/strings/?num=1&len={length}&digits={("off", "on")[digits]}&' \
          f'upperalpha={("off", "on")[uppercase]}&loweralpha={("off", "on")[lowercase]}&' \
          f'unique=on&format=plain&rnd=new'

    resp = requests.get(url)

    return resp.text.strip()


def rand_seed():
    time_now = datetime.now()
    seed_time_now = int(time_now.strftime("%y%m%d%H%M%S%f"))
    return seed_time_now if random() > 0.5 else -seed_time_now
