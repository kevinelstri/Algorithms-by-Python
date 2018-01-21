# coding:utf-8

'''
链表: 结点，next
'''


# 创建链表的节点，链表节点包括data和next
class LinkList(object):
    def __init__(self, x):
        self.data = x
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


# 在链表上进行操作，使用链表的节点进行处理
class OrderList(LinkList):
    def __init__(self, x):
        self.head = x
        self.next = None

    def is_empty(self):
        return self.head is None

    def add(self, val):
        temp = LinkList(val)
        current = self.head
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
            if previous.get_data() < val and (val <= current.get_data()):
                previous.set_next(temp)
                previous = previous.get_next()
                previous.set_next(current)
            else:
                current = current.get_next()
        current.set_next(temp)

    def size(self):
        current = self.head
        # print current.get_data()
        current = current.get_next()
        # print current.get_data()
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, val):
        current = self.head
        while current is not None:
            if current.get_data() == val:
                return True
            else:
                current = current.get_next()
            return False
        return False


if __name__ == '__main__':
    x = OrderList(1)
    print(x.is_empty())
    x.add(3)
    x.add(4)
    x.add(5)
    print(x.is_empty())
    print(x.search(5))
    print(x.size())
