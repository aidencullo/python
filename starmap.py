from itertools import starmap
import operator

def print_all(*args):
    print(args)

list(starmap(print_all, [(2,3), (4,5,6)]))  # [6, 20]

print(list(starmap(operator.mul, [(2,3),(4,5)])))  # [6, 20]
print(list(map(sum, [(2,3),(4,5)])))  # [6, 20]
