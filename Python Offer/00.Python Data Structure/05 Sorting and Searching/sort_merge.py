# coding:utf-8

'''
归并排序：二分法，递归排序
'''


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = int(len(nums) / 2)
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


if __name__ == '__main__':
    nums = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    print mergeSort(nums)
