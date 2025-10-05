from number_filter import filter_divisible_by_three


def test_filter_divisible_by_three():
    assert filter_divisible_by_three([1, 3, 4, 6, 7, 9, 10]) == [3, 6, 9]
    assert filter_divisible_by_three([2, 4, 5, 7]) == []
    assert filter_divisible_by_three([0, 3, 6, 12]) == [0, 3, 6, 12]
    assert filter_divisible_by_three([]) == []
    print("All test cases for filter_divisible_by_three function passed!")
