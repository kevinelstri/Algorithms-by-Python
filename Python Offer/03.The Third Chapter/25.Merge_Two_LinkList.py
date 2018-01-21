# coding:utf-8

'''
合并两个递增排序的链表，保持合并后的链表仍然是排序的
'''


class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def MergeTwoLinklist(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            return None
        elif pHead1 is None and pHead2 is not None:
            return pHead2
        elif pHead1 is not None and pHead2 is None:
            return pHead1
        else:
            Head = pHead1
            while pHead1.next is not None:
                last1 = pHead1.next
                if (pHead2.val >= pHead1.val) and pHead2.val <= last1.val:
                    last2 = pHead2.next
                    pHead1.next = pHead2
                    pHead2.next = last1
                    if last2 is not None:
                        pHead2 = last2
                    else:
                        pHead1.next = pHead2
                pHead1 = pHead1.next
            pHead1.next = pHead2
        return Head


node1 = LinkList(10)
node2 = LinkList(12)
node3 = LinkList(14)
node4 = LinkList(16)
node1.next = node2
node2.next = node3
node3.next = node4

link1 = LinkList(11)
link2 = LinkList(13)
link3 = LinkList(15)
link4 = LinkList(17)
link1.next = link2
link2.next = link3
link3.next = link4

S = Solution()
xx = S.MergeTwoLinklist(node1, link1)
while xx.next is not None:
    print xx.val
    xx = xx.next
