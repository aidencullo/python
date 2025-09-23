def filter_divisible_by_three(lst):
    is_divisible_by_three = lambda x: x % 3 == 0
    return list(filter(is_divisible_by_three, lst))
