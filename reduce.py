from functools import reduce
import operator

reduce(lambda acc, x: acc + x, [1, 2, 3], 0)
