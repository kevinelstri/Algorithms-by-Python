# coding:utf-8

'''
插入排序：一个一个插入排序
'''


def insertSort(nums):
    if len(nums) <= 0 or nums == []:
        return None
    for i in range(1, len(nums)):
        while i >= 1:
            if nums[i] > nums[i - 1]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
            i -= 1
    return nums


if __name__ == '__main__':
    nums = [2, 3, 51, 13, 5, 62, 4]
    print insertSort(nums)
