# coding:utf-8


def sum_list(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_list(nums[1:])


nums = [2, 4, 6, 8, 10]
print sum_list(nums)
