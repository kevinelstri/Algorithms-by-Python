# coding:utf-8

'''
两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点
'''

'''
方法二：比较两个栈的长度，使用两个指针分别前进不同的步伐，
当两个指针相同时，就是相同元素位置
'''


class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def Count(self, pHead):
        # 计算长度
        count = 1
        while pHead.next is not None:
            pHead = pHead.next
            count += 1
        return count

    def FindCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None

        S = Solution()
        count1 = S.Count(pHead1)
        count2 = S.Count(pHead2)

        # 双指针分别移动
        if count1 >= count2:
            dis = count1 - count2  # 距离
            diss = dis  # 标记
            while diss != 0:
                pHead1 = pHead1.next
                diss -= 1
            while pHead2.next is not None:
                con = 1  # 共同向前移动的距离
                if pHead1.val == pHead2.val:
                    return dis + con, con
                else:
                    pHead1 = pHead1.next
                    pHead2 = pHead2.next
                    con += 1
        else:
            dis = count2 - count1  # 距离
            # print dis
            diss = dis  # 标记
            while diss != 0:
                pHead2 = pHead2.next
                diss -= 1
            con = 1  # 共同向前移动的距离
            while pHead1.next is not None:
                if pHead1.val == pHead2.val:
                    return dis + con, con
                else:
                    pHead1 = pHead1.next
                    pHead2 = pHead2.next
                    con += 1


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

    # print link1.val
    s = Solution()
    xx = s.FindCommonNode(node1, link1)
    yy = s.FindCommonNode(list1, link1)
    zz = s.FindCommonNode(list1, list2)
    print xx
    print yy
    print zz
