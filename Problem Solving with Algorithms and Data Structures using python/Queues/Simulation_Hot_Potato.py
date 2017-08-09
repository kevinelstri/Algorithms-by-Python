# coding:utf-8

from Queues import Queue


# Simulation Hot Potato
def Hot(name_list, num):
    q = Queue()
    if len(name_list) == 0:
        return None
    else:
        for name in name_list:
            q.enqueue(name)
        while num >= 1:
            first = q.dequeue()
            q.enqueue(first)
            num -= 1
        return q.dequeue()


name_list = [1, 2, 3, 4]
num = 7
print Hot(name_list, num)
