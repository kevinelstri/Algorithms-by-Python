# coding:utf-8

'''
删除链表的节点
给定单向链表的头指针和一个节点指针，定义一个函数在O（1）时间内删除该节点
'''


class LinkList(object):
    def __init__(self, x):
        self.data = x
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class List(LinkList):
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = LinkList(data)
        self.head = temp
        current = self.head
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
            if previous.get_data() < data and (data <= current.get_data()):
                previous.set_next(data)
                previous = previous.get_next()
                previous.set_next(current)
            else:
                current = current.get_next()
        current.set_next(data)

    def size(self):
        current = self.head
        count = 0
        while current.get_next() is not None:
            current = current.get_next()
            count += 1
        return count

    # 常规做法
    def search(self, data):
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
            return False
        return False

    # 常规做法：O(n)
    def delete(self, data):
        current = self.head
        if current.get_next() is None:
            return False
        while current.get_next() is not None:
            middle = current.get_next()
            if middle.get_data() == data:
                last = middle.get_next()
                current.set_next(last)
                del middle
                return True
            else:
                current = current.get_next()
            return False
        return False

    # 删除一个节点的O(1)操作(节点指针已知的情况下)：
    # 将后一个节点向前复制，然后删除后一个节点所在的位置
    # 不需要遍历查找节点了
    def delete_copy(self, data):
        if self.head is None:
            return None
        current = self.head
        if current.get_data() == data:
            del current
            self.head = None
        if current.get_next() is None:
            if current.get_data() == data:
                current.set_data(None)
        else:
            last = current.get_next()
            current.set_data(last.get_data())
            current.set_next(last.get_next())
            del last


if __name__ == '__main__':
    List()
