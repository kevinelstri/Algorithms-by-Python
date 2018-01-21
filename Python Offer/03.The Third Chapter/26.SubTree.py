# coding:utf-8

'''
树的子结构：
输入两颗二叉树AB，判断B是不是A的子结构
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def HasSubTree(self, pRoot1, pRoot2):

        result = False

        if not pRoot1 or not pRoot2:
            return result

        if pRoot1.val == pRoot2.val:
            result = self.DoesTreeHasTree2(pRoot1, pRoot2)
        if not result:
            result = self.HasSubTree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubTree(pRoot1.right, pRoot2)
        return result

    def DoesTreeHasTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTreeHasTree2(pRoot1.right, pRoot2.right) and self.DoesTreeHasTree2(pRoot1.left, pRoot2.left)


if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print S.HasSubTree(pRoot1, pRoot8)
