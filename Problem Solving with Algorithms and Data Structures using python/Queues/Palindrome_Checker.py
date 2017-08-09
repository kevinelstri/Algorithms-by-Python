# coding:utf-8

from Deques import deque


# Palindrome Checker:回文检查程序,字符串关于中间对称
def checker_palindrome(ch_string):
    d = deque()
    for c in ch_string:
        d.add_front(c)
    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
        return True
    return False

ch_string = 'rr'
print checker_palindrome(ch_string)
