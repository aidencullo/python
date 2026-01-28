from functools import reduce
import operator

lst = [range(i) for i in range(10)]

reduce(lambda acc, x: acc + len(x), lst, 0)
