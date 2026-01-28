from functools import reduce
import operator

r = reduce(operator.add, range(10))
print(r)
