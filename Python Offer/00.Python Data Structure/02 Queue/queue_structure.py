# coding:utf-8

'''
建立队列
'''


class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())


