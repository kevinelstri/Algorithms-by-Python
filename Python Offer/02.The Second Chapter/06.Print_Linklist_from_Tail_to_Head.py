# coding:utf-8

'''
从尾到头打印 单链表
方法一：使用栈
方法二：使用递归
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Link(object):
    @staticmethod
    def link(values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print e
        return head.next


# 使用栈来存储，然后再输出
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print stack.pop()


# 使用递归next来输出
def print_links_recursion(links):
    if links:
        print_links_recursion(links.next)
        print links.val


if __name__ == '__main__':
    links = Link.link([1, 2, 3, 4, 5])
    print_links(links)
    print_links_recursion(links)
