# coding:utf-8

'''
将两个栈的操作写到main中，效果会差一些
优化方案：直接定义两个不同的栈，将栈之间的操作写入到队列类的创建中，main函数中只进行队列数据的进入和输出
'''


class MyQueue(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()


if __name__ == '__main__':
    p = MyQueue()
    q = MyQueue()

    p.push(2)
    p.push(3)

    q.push(p.pop())
    q.push(p.pop())

    print q.pop()
    print q.pop()
