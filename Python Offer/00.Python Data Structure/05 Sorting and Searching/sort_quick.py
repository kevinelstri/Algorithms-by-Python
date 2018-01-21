# coding:utf-8

'''
快速排序：一半一半排序，递归排序
'''


def partion(nums, left, right):
    key = nums[left]
    while left < right:
        while left < right and (nums[right] >= key):
            right -= 1
        nums[left] = nums[right]
        print nums
        while left < right and (nums[left] <= key):
            left += 1
        nums[right] = nums[left]
        nums[left] = key
        print nums
    print '-------------'
    print left, right  # 相等的情况下，不能继续了
    print '-------------'
    return left


def quicksort(nums, left, right):
    if left < right:
        p = partion(nums, left, right)
        quicksort(nums, left, p - 1)
        quicksort(nums, p + 1, right)
    return nums


if __name__ == '__main__':
    nums = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    print quicksort(nums, 0, len(nums)-1)
