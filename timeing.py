import time


def quadratic(n):
    x = 0

    for i in range(n):
        for j in range(i, n):
            x += 1


def timed_quadratic(n):
    t0 = time.time()
    quadratic(n)
    t1 = time.time()
    return t1 - t0


def timed_quadratic_suite():
    for i in range(10):
        factor = 1000
        t = timed_quadratic(i * factor)
        print(t, i * factor)


timed_quadratic_suite()
