# coding:utf-8

'''
数字在排序数组中出现的次数
输入：[1,2,3,3,3,3,4,5,6], 3
输出：4
'''


class Solution(object):
    index = []

    # 递归二分法，用于在有序数组中查找数字，但是无法确定数字的位置
    def TwoSplitMethod(self, array, num):
        if array is None or len(array) == 0:
            return None
        first = 0
        end = len(array) - 1
        index = (first + end) / 2
        if array[index] == num:
            self.index.append(index)
            if array[index - 1] == num:
                self.TwoSplitMethod(array[:index], num)
            elif array[index + 1] == num:
                self.TwoSplitMethod(array[index + 1:], num)
        else:
            if array[index] > num:
                self.TwoSplitMethod(array[:index], num)
            else:
                self.TwoSplitMethod(array[index + 1:], num)
        return self.index

    # 循环操作二分法，可以确定数字的位置
    def BinarySearch(self, array, num):
        if array is None or len(array) == 0:
            return None
        first = 0
        end = len(array) - 1
        while first <= end:
            index = (first + end) / 2
            if array[index] > num:
                end = index - 1
            elif array[index] < num:
                first = index + 1
            else:
                # if array[index - 1] == num:
                #     end = index - 1
                # if array[index + 1] == num:
                #     first = index + 1
                return index
                # self.index.append(index)
        return -1


if __name__ == '__main__':
    number = [1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]

    num = 3
    s = Solution()
    # print s.TwoSplitMethod(number, num)
    print s.BinarySearch(number, num)
