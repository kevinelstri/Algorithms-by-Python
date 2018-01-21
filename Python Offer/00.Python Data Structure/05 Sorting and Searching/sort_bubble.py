# coding:utf-8

'''
冒泡排序：两个两个比较大小，不断循环
'''


def bubbleSort(nums):
    if len(nums) <= 0 or nums == []:
        return None
    count = len(nums)
    while count > 0:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        count -= 1
    return nums


if __name__ == '__main__':
    nums = [2, 3, 51, 13, 5, 62, 4]
    print bubbleSort(nums)
