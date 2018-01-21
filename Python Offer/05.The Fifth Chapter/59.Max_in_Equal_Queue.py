# coding:utf-8

'''
队列的最大值
1、滑动窗口最大值，给定一个数组和滑动窗口的大小，找出所有滑动窗口里的最大值
2、队列的最大值,定义一个队列并实现函数max得到队列里的最大值，max,push和pop时间复杂度为O(1)
'''


# 1、滑动窗口的最大值
def MaxInWindow(array, k):
    if array is None or len(array) <= 0:
        return None
    if k <= 0:
        return None
    if k >= len(array):
        return max(array)
    first = 0
    last = k
    while last <= len(array):
        print max(array[first:last]),
        first += 1
        last += 1


# 队列最大值
class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def push(self, data):
        self.queue.insert(0, data)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def append(self, data):
        self.queue.append(data)

    def delte(self):
        return self.queue.pop(0)


def MaxInQueue(array):
    q = Queue()
    max = array[0]
    q.push(max)
    for i in range(1, len(array)):
        if array[i] > max and q.size() == 1:
            max = array[i]
            q.push(max)
            q.pop()
        elif array[i] > max and q.size() == 2:
            max = array[i]
            q.push(max)
        elif array[i] < max and q.size() == 1:
            q.append(array[i])
        elif array[i] < max and q.size() == 3:
            q.pop()
            q.pop()
            q.append(array[i])
        elif array[i] < max and q.size() == 2:
            q.delte()
            q.push(array[i])
    while q.size() != 0:
        print q.pop(),


if __name__ == '__main__':
    array = [2, 3, 4, 2, 6, 2, 5, 1]
    k = 3
    # MaxInWindow(array, k)
    print '------------------------------'
    queue = [1, 2, 3, 4]
    MaxInQueue(array)
