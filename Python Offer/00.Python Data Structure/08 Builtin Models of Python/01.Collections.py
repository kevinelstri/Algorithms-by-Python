# coding:utf-8

'''
python内置模块：collections

'''

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

'''
使用nametuple()来创建tuple对象
'''
# 点的坐标表示：x坐标，y坐标
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y

# 圆的表示:半径，x轴坐标，y坐标
Circle = namedtuple('Circle', ['r', 'x', 'y'])

'''
使用deque()来创建队列和栈对象
'''
q = deque([1, 2, 3])
q.append(6)  # 添加元素
q.appendleft(0)  # 左边添加元素
print q  # deque([0, 1, 2, 3, 6])
q.pop()  # 删除元素
q.popleft()  # 左边删除元素
print q  # deque([1, 2, 3])

'''
使用defaultdict()来调用无key值得dict
'''
d = defaultdict(lambda: 'value')  # 建立一个默认的key-value键值对，key为未知的
d['key1'] = 'value1'
print d['key1']  # 有key值时，输出对应的key值 'value1'
print d['key2']  # 无key值时，输出默认的key值 'value'

'''
使用OrederedDict()来保持字典的顺序，将输入和输出的顺序一致
插入顺序与输出顺序相同
'''
d = dict([('a', 3), ('b', 2), ('c', 1), ('d', 4)])
print d
d = OrderedDict([('a', 3), ('b', 2), ('c', 1), ('d', 4)])
print d

'''
Counter计数器:简化计数的计算过程，循环中将字符进行一一对应，来实现字符串中字符的统计
将统计结果按照递减顺序排列
'''
c = Counter()
ch = 'gameoverprogramming'
for i in ch:
    c[i] = c[i] + 1
print c  # Counter({'g': 3, 'm': 3, 'r': 3, 'a': 2, 'e': 2, 'o': 2, 'i': 1, 'n': 1, 'p': 1, 'v': 1})
print c['a']  # 2
