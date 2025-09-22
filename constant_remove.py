def constant_remove(num, nums):
    removed = 0
    for i, el in enumerate(nums):
        if el == num:
            removed += 1
        else:
            nums[i - removed] = el
    for _ in range(removed):
        nums.pop()


def test(num, nums):
    local_nums = list(nums)
    local_nums = nums[:]
    local_nums = nums.copy()
    expected = list(nums)
    expected.remove(num)
    constant_remove(num, local_nums)
    assert local_nums == expected

test(0, [0])
test(0, list(range(10)))
test(0, list(range(100)))
test(1, [2, 3, 1])
