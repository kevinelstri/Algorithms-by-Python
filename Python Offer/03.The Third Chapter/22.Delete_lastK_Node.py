# coding:utf-8

'''
链表中倒数第K个节点
输入一个链表，输出该链表中倒数第K个节点
从1开始计数，尾节点为倒数第1个节点
'''

'''
方法一：从链表头走到尾，然后从尾节点向前输出
方法二：双指针，前一个指针先走，后一个指针隔K步再走
'''


class LinkNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution(object):
    def findK(self, head, k):
        if head is None or k == 0:
            return None

        first = head
        for i in range(k - 1):
            if first.next:
                first = first.next
            else:
                return None

        second = head
        while first.next:
            first = first.next
            second = second.next
        return second


if __name__ == '__main__':
    node1 = LinkNode(10)
    node2 = LinkNode(11)
    node3 = LinkNode(12)
    node1.next = node2
    node2.next = node3

    s = Solution()
    print s.findK(node1, 3).data
