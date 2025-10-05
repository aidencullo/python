from string_filter import filter_strs


def test_filter_strs():
    assert filter_strs(["aiden", "tanner"]) == ["aiden"]
    assert filter_strs(["apple", "banana", "avocado"]) == ["apple", "avocado"]
    assert filter_strs(["cherry", "berry", "date"]) == []
    assert filter_strs(["ant", "anchor", "boat", "aqua"]) == ["ant", "anchor", "aqua"]
    assert filter_strs([]) == []
    print("All test cases for filter_strs function passed!")
