# coding:utf-8

'''
链表中环的入口节点
一个链表包含环，找到环所在的位置
'''

'''
方法：先判断链表中有环（双指针），在计算环的位置（双指针，其中环的距离为步长）
'''


class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 判断环形，并计算环形节点距离
    def is_circle(self, pHead):
        if pHead is None:
            return None
        if pHead.next is None:
            return None

        first = pHead
        second = pHead
        while first.next != second:
            if first.next is None:
                return False
            first = first.next
            first = first.next
            second = second.next
        CircleNode = second.val  # 链表中两个指针相遇的位置
        count = 1
        while second.next.val != CircleNode:
            second = second.next
            count += 1
        result = (CircleNode, count)  # circleNode表示相遇位置，count表示环形链表中节点最长距离
        return result

    def FindCircleNode(self, pHead):
        if pHead is None:
            return None
        if pHead.next is None:
            return None
        S = Solution()
        result = S.is_circle(pHead)  # type(result)='tuple'
        if result is False:
            return False
        else:  # 当存在环，此时来查找环开始的位置
            dis = result[1]
            first = pHead
            second = pHead
            while dis != 0:
                first = first.next
                dis -= 1
            while second.val != first.val:
                first = first.next
                second = second.next
            return first.val


if __name__ == '__main__':
    node1 = LinkList(1)
    node2 = LinkList(2)
    node3 = LinkList(3)
    node4 = LinkList(4)
    node5 = LinkList(5)
    node6 = LinkList(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3

    link1 = LinkList(8)
    link2 = LinkList(9)
    link3 = LinkList(10)
    link4 = LinkList(11)
    link5 = LinkList(12)
    link1.next = link2
    link2.next = link3
    link3.next = link4
    link4.next = link5

    list1 = LinkList(0)

    s = Solution()
    xx = s.FindCircleNode(node1)
    yy = s.FindCircleNode(link1)
    zz = s.FindCircleNode(list1)
    print xx
    print yy
    print zz
