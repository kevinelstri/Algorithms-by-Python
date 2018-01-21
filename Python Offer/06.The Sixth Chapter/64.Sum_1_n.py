# coding:utf-8

'''
求1+2+3+...+n的和
要求不能使用乘除法,for,while,if,else,switch,case等关键字以及条件判断语句
'''


class Solution(object):
    def sum0(self, n):
        return 0

    def sum(self, n):
        fun = {False: self.sum0, True: self.sum}  # fun为字典，key值为bool类型，value为函数
        return n + fun[not not n](n - 1)  #


if __name__ == '__main__':
    s = Solution()
    print s.sum(5)
