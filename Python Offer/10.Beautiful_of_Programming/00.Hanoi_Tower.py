# coding:utf-8

'''
汉诺塔：
三根柱子，其中一根柱子上包括1~64大小的圆盘，移动圆盘，
将所有圆盘移动到另一个柱子上，并随时保持小的在上，大的在下
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class Solution(object):
    def HanioTower(self, s1, s2, s3):
        while s1.size() != 0:
            data = s1.pop()
            if s2.size() == 0:
                s2.push(data)
            else:
                s3.push(data)
            while s1.size() != 0 and s2.size() != 0:
                s3.push(data)
                s3.push(s2.pop())
        print s1.size()
        print s2.size()
        print s3.size()


if __name__ == '__main__':
    # 初始化三个栈，用于栈中数据的移动
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()

    # 创建数据，并写入到第一个栈中
    num = []
    for i in range(1, 65):
        num.append(i)

    for i in range(len(num) - 1, -1, -1):
        s1.push(num[i])
    # print s1.peek()  # 栈的顶端：1
    # print s1.size()  # 栈的大小：64

    # 使用Solution类来对汉诺塔问题进行处理
    s = Solution()
    s.HanioTower(s1, s2, s3)
