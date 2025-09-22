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
    expected = list(nums)
    expected.remove(num)
    constant_remove(num, local_nums)
    assert local_nums == expected

test(0, [0])
test(0, list(range(10)))
