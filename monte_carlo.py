import random
import time
import numpy as np


def forWayCircle(n):
    time_start = time.perf_counter()

    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1

    pi = 4 * count / n

    time_end = time.perf_counter()

    return pi, time_end - time_start


def numpyWayCircle(n):
    time_start = time.perf_counter()
    count = 0
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)

    z = x**2 + y**2
    count = np.sum(z <= 1)

    pi = 4 * count / n

    time_end = time.perf_counter()

    return pi, time_end - time_start, x, y, z


def forWayBall(n):
    time_start = time.perf_counter()

    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        if x**2 + y**2 + z**2 <= 1:
            count += 1

    pi = 8 * count / n

    time_end = time.perf_counter()

    return pi, time_end - time_start


def numpyWayBall(n):
    time_start = time.perf_counter()
    count = 0
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    z = np.random.uniform(-1, 1, n)

    w = x**2 + y**2 + z**2
    count = np.sum(z <= 1)

    pi = 8 * count / n

    time_end = time.perf_counter()

    return pi, time_end - time_start, x, y, z, w


if __name__ == '__main__':
    n = 10000000

    forWayCircle(n)
    numpyWayCircle(n)
    forWayBall(n)
    numpyWayBall(n)
