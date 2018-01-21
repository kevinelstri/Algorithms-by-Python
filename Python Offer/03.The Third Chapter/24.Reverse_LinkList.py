# coding:utf-8

'''
反转链表
使用三个指针
'''


class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def ReverseLinkList(self, pHead):
        if pHead is None:
            return None
        elif pHead.next is None:
            return pHead
        else:
            middle = pHead.next
            pHead.next = None
            last = middle.next
            while middle:
                middle.next = pHead
                pHead = middle
                middle = last
                if middle:
                    last = middle.next
            return pHead


node1 = LinkNode(10)
node2 = LinkNode(11)
node3 = LinkNode(12)
node4 = LinkNode(13)
node5 = LinkNode(14)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
xx = s.ReverseLinkList(node1)
# print xx
print xx.next.next.val
