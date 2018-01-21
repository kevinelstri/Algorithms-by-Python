# coding:utf-8

'''
给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间删除节点
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution(object):
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

            # 删除中间节点
        if pToBeDeleted.next is not None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()
            # 删除头节点
        elif pListHead == pToBeDeleted:
            pListHead.__del__()
            pToBeDeleted.__del__()
        else:
            # 删除尾节点：从头到尾遍历
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node4 = ListNode(13)
node1.next = node2
node2.next = node3
node3.next = node4

s = Solution()
s.DeleteNode(node1, node3)
print node3.val
print node2.val


s.DeleteNode(node1, node4)
# print node4.val
# s.DeleteNode(node1, node1)
# print node1.val
