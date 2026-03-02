import random
import time


def forWay(n):
    time_start = time.perf_counter()

    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1

    pi = 4 * count / n

    time_end = time.perf_counter()

    print(pi)
    print(time_end - time_start)


n = 1000000
forWay(n)
