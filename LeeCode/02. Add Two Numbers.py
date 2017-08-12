# codinng:utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def getval(self):
    #     return self.val
    #
    # def getnext(self):
    #     return self.next
    #
    # def setval(self, newval):
    #     self.val = newval
    #
    # def setnext(self, newnext):
    #     self.next = newnext


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = str()
        s2 = str()
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
        s1 = int(s1)
        s2 = int(s2)
        sum = s1 + s2
        sum = str(sum)
        sum = sum[::-1]
        ret = ListNode(sum[0])
        cur1 = ret
        for i in range(1,len(sum)):
            cur1.next = ListNode(sum[i])
            cur1 = cur1.next
        return ret

l1 = [2, 4, 3]
l2 = [5, 6, 4]
s = Solution()
print s.addTwoNumbers(l1, l2)
