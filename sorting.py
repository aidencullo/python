# sort dict by increasing key and decreasing value

from collections import Counter
hello = "hello"
d = { i: x for i, x in enumerate(hello)}
counter = Counter(hello)
counter_list = list(counter)
sorted_tuples = sorted(counter.items(), key=lambda key_value: key_value[1])
sorted_tuples = sorted(d.items())
print(sorted_tuples)

from functools import reduce
import operator
import random

[random.randint(1, 100) for i in range(100)]



def min_from_reduce():
    randoms = random.choices(range(100), k=10)
    print(randoms)
    return reduce(lambda x, y: x if x < y else y, randoms)

min_from_reduce()
