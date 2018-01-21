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
    # 树：递归算法
    def PathSum(self, pRoot, N):
        if pRoot is None:
            return []
        if pRoot.left is None and pRoot.right is None:
            if pRoot.val == N:
                return [[pRoot.val]]  # 不同的分支要放到不同的list中
                # print type([pRoot.val])
            else:
                return []  # 由于list不能加bool类型，因此使用[]来表示
        a = self.PathSum(pRoot.left, N - pRoot.val) + self.PathSum(pRoot.right, N - pRoot.val)
        # print type(a)
        return [[pRoot.val] + i for i in a]


if __name__ == '__main__':
    pNode1 = BinaryTreeNode(10)
    pNode2 = BinaryTreeNode(5)
    pNode3 = BinaryTreeNode(12)
    pNode4 = BinaryTreeNode(4)
    pNode5 = BinaryTreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5

    s = Solution()
    print s.PathSum(pNode1, 22)
