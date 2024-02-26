def rec_func(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + rec_func(nums, idx + 1)


nums = [int(x) for x in input().split()]
print(rec_func(nums))