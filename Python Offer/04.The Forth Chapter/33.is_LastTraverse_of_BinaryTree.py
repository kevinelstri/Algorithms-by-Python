# coding:utf-8

'''
二叉搜索树的后序遍历序列
输入一个数组，判断该数组是不是二叉搜索树的后序遍历序列
'''


class Solution(object):
    def isLastTraverseBineryTree(self, Array):
        if not Array:
            return False
        length = len(Array)
        root = Array[-1]

        for i in range(length):
            if Array[i] > root:
                break
        for j in range(i, length):
            if Array[j] < root:
                return False
        left = True
        if i > 0:
            left = self.isLastTraverseBineryTree(Array[:i])
        right = True
        if j < length - 1:
            right = self.isLastTraverseBineryTree(Array[j:])
        return left and right


if __name__ == '__main__':
    Array = [5, 7, 6, 9, 11, 10, 8]
    Array2 = [1, 2, 3, 4, 5, 6, 7, 8]
    Array3 = [5, 6, 9, 11, 10, 8]
    Array4 = [4, 6, 7, 1, 5]
    s = Solution()
    print s.isLastTraverseBineryTree(Array)
    print '-------------------------'
    print s.isLastTraverseBineryTree(Array2)
    print '-------------------------'
    print s.isLastTraverseBineryTree(Array3)
    print s.isLastTraverseBineryTree(Array4)
