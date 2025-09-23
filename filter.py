from functools import partial

# Function to filter strings starting with 'a'
def starts_with(s, prefix):
    return s.startswith(prefix)

def filter_strs(strs):
    starts_with_a = partial(starts_with, prefix='a')
    lst = list(filter(starts_with_a, strs))
    return lst

# Tests for filter_strs
assert filter_strs(["aiden", "tanner"]) == ["aiden"]
assert filter_strs(["apple", "banana", "avocado"]) == ["apple", "avocado"]
assert filter_strs(["cherry", "berry", "date"]) == []
assert filter_strs(["ant", "anchor", "boat", "aqua"]) == ["ant", "anchor", "aqua"]
assert filter_strs([]) == []

print("All test cases for filter_strs function passed!")

from functools import partial

# Function to filter numbers divisible by 3
def filter_divisible_by_three(lst):
    is_divisible_by_three = lambda x: x % 3 == 0
    return list(filter(is_divisible_by_three, lst))

# Tests for filter_divisible_by_three
assert filter_divisible_by_three([1, 3, 4, 6, 7, 9, 10]) == [3, 6, 9]
assert filter_divisible_by_three([2, 4, 5, 7]) == []
assert filter_divisible_by_three([0, 3, 6, 12]) == [0, 3, 6, 12]
assert filter_divisible_by_three([]) == []

print("All test cases for filter_divisible_by_three function passed!")
