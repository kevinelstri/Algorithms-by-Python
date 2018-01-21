# coding:utf-8

'''
选择排序：选择其中一个进行比较，直到所有全部排序为止
'''


def selectSort(nums):
    if len(nums) <= 0 or nums == []:
        return None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    return nums


if __name__ == '__main__':
    nums = [2, 3, 51, 13, 5, 62, 4]
    print selectSort(nums)
