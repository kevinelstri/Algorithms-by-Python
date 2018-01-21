# coding:utf-8

'''
二叉树中和为某一值的路径
输入一个二叉树和一个整数，打印二叉树中节点值得和为输入整数的所有路径，
从根节点开始往下一直到叶节点所经过的节点形成一条路径
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def PathSum(self, pRoot, N):
        if pRoot is None:
            return []
        if pRoot.left is None and pRoot.right is None:
            if pRoot.val == N:
                return [[pRoot.val]]
            else:
                return []

        stack = []
        leftstack = self.PathSum(pRoot.left, N - pRoot.val)
        for i in leftstack:
            i.insert(0, pRoot.val)
            stack.append(i)

        rightstack = self.PathSum(pRoot.right, N - pRoot.val)
        for i in rightstack:
            i.insert(0, pRoot.val)
            stack.append(i)

        return stack


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(5)
    pRoot3 = BinaryTreeNode(12)
    pRoot4 = BinaryTreeNode(4)
    pRoot5 = BinaryTreeNode(7)

    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5

    s = Solution()
    print s.PathSum(pRoot1, 22)
