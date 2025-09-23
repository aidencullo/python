# Coding Challenge (Python) Write a function find_most_frequent(nums: list[int]) -> int that returns the integer appearing most frequently in a list. If there is a tie, return the smallest number. You have access to an AI coding assistant for hints.

from functools import partial
from collections import Counter
import operator

def find_most_frequent(nums: list[int]) -> int: # n time/space
    counter = Counter(nums)
    highest_frequency_num = max(counter, key=counter.get)
    highest_frequency = counter[highest_frequency_num]
    eq_max = partial(operator.eq, highest_frequency)
    most_frequent = [k for k, v in counter.items() if eq_max(v)]
    return min(most_frequent)


def test_find_most_frequent():
    assert find_most_frequent(reversed(range(5))) == 0
    assert find_most_frequent(range(10)) == 0
    assert find_most_frequent([0, 0, 1]) == 0
    assert find_most_frequent([0, 0, 1, 1]) == 0
    assert find_most_frequent([0, 1] * 2) == 0
    assert find_most_frequent(([0] * 5) + ([1] * 5)) == 0

test_find_most_frequent()
print("All test cases for find_most_frequent function passed!")
