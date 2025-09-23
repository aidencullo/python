# Given a list of strings, use filter to create a new list containing only the strings that start with the letter "a".

def filter_strs(strs):
    return list(filter(lambda s: s.startswith("a"), strs))


# Tests
assert filter_strs(["aiden", "tanner"]) == ["aiden"]
assert filter_strs(["apple", "banana", "avocado"]) == ["apple", "avocado"]
assert filter_strs(["cherry", "berry", "date"]) == []
assert filter_strs(["ant", "anchor", "boat", "aqua"]) == ["ant", "anchor", "aqua"]
assert filter_strs([]) == []

print("All tests passed!")
