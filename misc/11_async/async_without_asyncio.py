import time


tasks = []


def asyncio_sleep(n: int):
    time_start = time.time()
    while True:
        if time.time() - time_start >= n:
            return
        yield


def inf_print():
    i = 0
    while True:
        print(i)
        i += 1
        yield from asyncio_sleep(0.5)


def print_name(name: str):
    for i in name:
        print(i)
        yield from asyncio_sleep(0.5)


def event_loop():
    tasks.append(inf_print())
    tasks.append(print_name("thek4n"))


    while True:
        try:
            g = tasks.pop(0)
        except IndexError:
            break

        try:
            result = next(g)
        except StopIteration:
            pass
        else:
            tasks.append(g)


def main():
    event_loop()


if __name__ == "__main__":
    main()

