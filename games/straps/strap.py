#!/usr/bin/env python3

# погоны
from time import time
import os
from random import choice
from fuzzywuzzy import fuzz


def ryadovoy():
    print()

    print('-------------------')
    print('-                   --')
    print('-                   --')
    print('-                   --')
    print('-                   --')
    print('-                   --')
    print('-------------------')

    print()

    return 'рядовой'


def efreq():
    print()

    print('-------------------')
    print('-                   --')
    print('-     --            --')
    print('-        --         --')
    print('-     --            --')
    print('-                   --')
    print('-------------------')

    print()

    return 'ефрейтор'


def mserg():
    print()

    print('-------------------')
    print('-                   --')
    print('-     -- --         --')
    print('-        -- --      --')
    print('-     -- --         --')
    print('-                   --')
    print('-------------------')

    print()

    return 'младший сержант'


def serg():
    print()

    print('-------------------')
    print('-                   --')
    print('-     -- -- --      --')
    print('-        -- -- --   --')
    print('-     -- -- --      --')
    print('-                   --')
    print('-------------------')

    print()

    return 'сержант'


def userg():
    print()

    print('-------------------')
    print('-                   --')
    print('-       ----        --')
    print('-           ----    --')
    print('-       ----        --')
    print('-                   --')
    print('-------------------')

    print()

    return 'старший сержант'


def starsh():
    print()

    print('-------------------')
    print('-                   --')
    print('-    -   ----       --')
    print('-       -    ----   --')
    print('-    -   ----       --')
    print('-                   --')
    print('-------------------')

    print()

    return 'старшина'


def prapor():
    print()

    print('-------------------')
    print('-                   --')
    print('-                   --')
    print('-     *    *        --')
    print('-                   --')
    print('-                   --')
    print('-------------------')

    print()

    return 'прапорщик'


def stprapor():
    print()

    print('-------------------')
    print('-                   --')
    print('-                   --')
    print('-    *   *   *      --')
    print('-                   --')
    print('-                   --')
    print('-------------------')

    print()

    return 'старший прапорщик'


def mlet():
    print()

    print('-------------------')
    print('-                   --')
    print('-                   --')
    print('-======= * =========--')
    print('-                   --')
    print('-                   --')
    print('-------------------')

    print()

    return 'младший лейтенант'


def let():
    print()

    print('-------------------')
    print('-  *                --')
    print('-                   --')
    print('-===================--')
    print('-                   --')
    print('-  *                --')
    print('-------------------')

    print()

    return 'лейтенант'


def stlet():
    print()

    print('-------------------')
    print('-  *                --')
    print('-                   --')
    print('-========= * =======--')
    print('-                   --')
    print('-  *                --')
    print('-------------------')

    print()

    return 'старший лейтенант'


def cap():
    print()

    print('-------------------')
    print('-  *                --')
    print('-                   --')
    print('-====== * ==== * ===--')
    print('-                   --')
    print('-  *                --')
    print('-------------------')

    print()

    return 'капитан'


def major():
    print()

    print('-------------------')
    print('-                   --')
    print('-===================--')
    print('-         *         --')
    print('-===================--')
    print('-                   --')
    print('-------------------')

    print()

    return 'майор'


def dcol():
    print()

    print('-------------------')
    print('-                   --')
    print('-==== * ============--')
    print('-                   --')
    print('-==== * ============--')
    print('-                   --')
    print('-------------------')

    print()

    return 'подполковник'


def col():
    print()

    print('-------------------')
    print('-                   --')
    print('-==== * ============--')
    print('-           *       --')
    print('-==== * ============--')
    print('-                   --')
    print('-------------------')

    print()

    return 'полковник'


def genmajor():
    print()

    print('-------------------')
    print('-                   --')
    print('-       *           --')
    print('-      ***          --')
    print('-       *           --')
    print('-                   --')
    print('-------------------')

    print()

    return 'генерал майор'


def genlet():
    print()

    print('-------------------')
    print('-                   --')
    print('-    *    *         --')
    print('-   ***  ***        --')
    print('-    *    *         --')
    print('-                   --')
    print('-------------------')

    print()

    return 'генерал лейтенант'


def gencol():
    print()

    print('-------------------')
    print('-                   --')
    print('-    *    *    *    --')
    print('-   ***  ***  ***   --')
    print('-    *    *    *    --')
    print('-                   --')
    print('-------------------')

    print()

    return 'генерал полковник'


def genarm():
    print()

    print('-------------------')
    print('-                   --')
    print('- *    *    *    *  --')
    print('-***  ***  ***  *** --')
    print('- *    *    *    *  --')
    print('-                   --')
    print('-------------------')

    print()

    return 'генерал армии'


def marsh():
    print()

    print('-------------------')
    print('-                   --')
    print('-   * **     ***-   --')
    print('-    **        **   --')
    print('-   * **     ***-   --')
    print('-                   --')
    print('-------------------')

    print()

    return 'маршал'


lst = [ryadovoy, efreq, mserg, serg, userg, starsh, prapor, stprapor,
       mlet, let, stlet, cap, major, dcol, col, genmajor, genlet, gencol, genarm, marsh]


def clear():
    os.system(['cls', 'clear'][os.name == 'posix'])


class Timer:
    def __init__(self):
        self.__start_time = time()

    def duration(self):
        return time() - self.__start_time


class Game:

    mode = None
    points = 0

    def start(self):
        while 1:
            print('1. Обучение \n2. Экзамен')
            mode = input()

            if mode in ('1', '2'):
                self.mode = mode
                break

        if self.mode == '1':
            while True:
                self.get_zv()
        else:
            timer = Timer()

            for i in range(10):
                self.get_zv()

            elapsed = round(timer.duration())
            print(elapsed, 'секунд')
            if self.points < 9 or elapsed > 50:
                print('Не зачет')
            else:
                print(F'Сдал')
            input()

    def get_zv(self):
        func = choice(lst)
        x = func()

        if fuzz.ratio(x, input('Звание: ')) > 85:
            self.points += 1
            clear()
            print('Правильно', self.points)
        else:
            self.points -= 1
            clear()
            print('Не верно!', x, self.points)


if __name__ == '__main__':
    clear()
    game = Game()
    game.start()
