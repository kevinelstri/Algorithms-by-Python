# coding:utf-8

'''
两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点
'''

'''
方法一：使用两个栈来存储两个链表，比较两个栈的栈顶元素
'''


class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class Solution(object):
    def FindFirstCommonNode(self, pHead1, pHead2):
        s1 = Stack()
        s2 = Stack()
        if pHead1 is None or pHead2 is None:
            return None
        while pHead1.next is not None:
            s1.push(pHead1.val)
            pHead1 = pHead1.next
        while pHead2.next is not None:
            s2.push(pHead2.val)
            pHead2 = pHead2.next
        while s1.size() != 0 and s2.size() != 0:
            while s1.peek() == s2.peek():
                s1.pop()
                s2.pop()
                if s1.size() == 0 or s2.size() == 0:
                    return s1.size()+1, s2.size() + 1
            return s1.size() + 1, s2.size() + 1
        return None


if __name__ == '__main__':
    node1 = LinkList(0)
    node2 = LinkList(11)
    node3 = LinkList(12)
    # node4 = LinkList(13)
    # node5 = LinkList(14)
    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5

    list1 = LinkList(0)
    list2 = LinkList(0)

    link1 = LinkList(8)
    link2 = LinkList(9)
    link3 = LinkList(10)
    link4 = LinkList(11)
    link5 = LinkList(12)
    link1.next = link2
    link2.next = link3
    link3.next = link4
    link4.next = link5

    s = Solution()
    xx = s.FindFirstCommonNode(node1, link1)
    yy = s.FindFirstCommonNode(list1, link1)
    zz = s.FindFirstCommonNode(list1, list2)
    print xx
    print yy
    print zz
