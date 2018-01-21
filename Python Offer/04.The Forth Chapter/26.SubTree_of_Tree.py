# coding:utf-8

'''
树的子结构
输入两颗二叉树A和B， 判断B是不是A的子结构
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def DoesTreeHasTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTreeHasTree(pRoot1.right, pRoot2.right) and self.DoesTreeHasTree(pRoot1.left, pRoot2.left)

    def HasSubTree(self, pRoot1, pRoot2):
        result = False
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.DoesTreeHasTree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubTree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubTree(pRoot1.right, pRoot2)
        return result


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(8)
    pRoot2 = BinaryTreeNode(8)
    pRoot3 = BinaryTreeNode(7)
    pRoot4 = BinaryTreeNode(9)
    pRoot5 = BinaryTreeNode(2)
    pRoot6 = BinaryTreeNode(4)
    pRoot7 = BinaryTreeNode(7)

    # first
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = BinaryTreeNode(8)
    pRoot9 = BinaryTreeNode(9)
    pRoot10 = BinaryTreeNode(2)

    # second
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    s = Solution()
    xx = s.HasSubTree(pRoot1, pRoot8)
    print xx
