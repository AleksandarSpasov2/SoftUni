def sum_rec(nums, index=0):
    if index == len(nums) - 1:
        return nums[index]

    return nums[index] + sum_rec(nums, index + 1)


nums = [int(x) for x in input().split()]
print(sum_rec(nums))
