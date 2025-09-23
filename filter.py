# Given a list of strings, use filter to create a new list containing only the strings that start with the letter "a".

from functools import partial

def starts_with(s, prefix):
    return s.startswith(prefix)

def filter_strs(strs):
    starts_with_a = partial(starts_with, prefix='a')
    lst = list(filter(starts_with_a, strs))
    return lst


# Tests
assert filter_strs(["aiden", "tanner"]) == ["aiden"]
assert filter_strs(["apple", "banana", "avocado"]) == ["apple", "avocado"]
assert filter_strs(["cherry", "berry", "date"]) == []
assert filter_strs(["ant", "anchor", "boat", "aqua"]) == ["ant", "anchor", "aqua"]
assert filter_strs([]) == []

print("All tests passed!")
