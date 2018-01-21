# coding:utf-8

'''
用两个栈来实现队列
'''


class MyQueue(object):
    def __init__(self):
        self.stack = []  # 定义两个空栈
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)  # 压入数据到第一个栈中

    def pop(self):
        if self.stack2:
            return self.stack2.pop()  # 第二个栈不空时，从第二个栈中弹出数据
        while self.stack:
            self.stack2.append(self.stack.pop())  # 将第一个栈的数据压入第二个栈中
        return self.stack2.pop() if self.stack2 else 'The queue is null'


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print q.pop()
    print q.pop()
    print q.pop()
