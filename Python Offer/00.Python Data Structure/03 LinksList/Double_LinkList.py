# coding:utf-8

'''
双向链表：
'''


class Node(object):
    def __init__(self, value=None):  # 要么在建立节点结构的时候，给节点赋值
        self.data = value
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):  # 要么在建立链表时，创建一个空节点
        self.head = Node()  # 建立head节点，head.data=None，但是head!=None

    def insert(self, value):
        node = Node(value)
        if self.head.data is None:
            self.head = node
            self.head.next = node
            self.head.prev = node
        else:
            p = self.head
            while p.next != self.head:
                p = p.next
            node.next = self.head
            self.head.prev = node
            p.next = node
            node.prev = p

    def search(self, value):
        if not self.head.next:
            return None
        if self.head.data == value:
            return self.head
        temp = self.head.next
        while temp.data != value and temp.data != self.head.data:  # 双向链表是循环的
            temp = temp.next
        return temp

    def delete(self, value):
        ele = self.search(value)
        if not ele:
            return ValueError('delete error: the value not found!')
        ele.prev.next = ele.next
        ele.next.prev = ele.prev
        return ele.data


if __name__ == '__main__':
    value = [1, 2, 3, 4, 5]
    d = DoubleLinkList()
    # print d.head.data  # None
    for i in range(len(value)):
        d.insert(value[i])
    print(d.head.data)
    print(d.head.next.data)
    print(d.head.next.next.data)
    print(d.head.next.next.next.prev.data)
    print(d.head.prev.data)
