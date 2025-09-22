# Coding Challenge (Python) Write a function find_most_frequent(nums: list[int]) -> int that returns the integer appearing most frequently in a list. If there is a tie, return the smallest number. You have access to an AI coding assistant for hints.


# filter(func, iterable) returns an iterator of items where func(item) is truthy. Example: list(filter(lambda x: x%2, [1,2,3])) → [1,3].

from functools import partial
from collections import Counter
import operator

def find_most_frequent(nums: list[int]) -> int:
    counter = Counter(nums)
    highest_frequency = max(counter.values())
    eq_max = partial(operator.eq, highest_frequency)
    most_frequent = [k for k, v in counter.items() if eq_max(v)]
    return min(most_frequent)


assert find_most_frequent(reversed(range(5))) == 0
assert find_most_frequent(range(10)) == 0
assert find_most_frequent([0, 0, 1]) == 0
assert find_most_frequent([0, 0, 1, 1]) == 0
assert find_most_frequent([0, 1] * 2) == 0
assert find_most_frequent(([0] * 5) + ([1] * 5)) == 0
