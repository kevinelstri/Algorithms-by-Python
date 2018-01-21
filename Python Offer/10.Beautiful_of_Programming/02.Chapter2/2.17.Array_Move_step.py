# coding:utf-8

'''
2.17数组循环移位
设计一个算法，把一个含有N个元素的数组循环右移K位，要求时间复杂度为O(N)，且只允许使用两个附加变量
'''


class Node(object):
    def __init__(self, value=None):  # 要么在建立节点结构的时候，给节点赋值
        self.data = value
        self.prev = None
        self.next = None


# 双链表
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


# 移动
def MoveArray(array, k):
    d = DoubleLinkList()
    for i in range(len(array)):
        d.insert(array[i])
    s = ''
    if k == 0:
        s += d.head.data
        p = d.head.next
        while p.next != d.head.next:
            s += p.data
            p = p.next
    elif k > 0:
        p = d.head
        while k != 0:
            p = p.next
            k -= 1
        s += p.data
        q = p.next
        while q.next != p.next:
            s += q.data
            q = q.next
    elif k < 0:
        p = d.head
        while k != 0:
            p = p.prev
            k += 1
        s += p.data
        q = p.next
        while q.next != p.next:
            s += q.data
            q = q.next
    return s


if __name__ == '__main__':
    k = -5
    array = ['a', 'b', 'c', 'd']
    print MoveArray(array, k)
