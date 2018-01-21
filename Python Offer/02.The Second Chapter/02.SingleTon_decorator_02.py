# coding:utf-8

'''
使用decoretor装饰器来实现单例模式
'''

from functools import wraps


def singleTon(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single


@singleTon
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)

    print s == t  # True
    print s is t  # True

    print s.a  # 1
    print t.a  # 1

    print s.val  # 123
    print t.val  # 123
