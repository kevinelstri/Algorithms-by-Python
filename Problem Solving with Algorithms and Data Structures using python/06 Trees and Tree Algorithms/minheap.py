# coding:utf-8

import math


class minheap:
    MIN_HEAP = True

    def __init__(self, nums=None):  # 初始化，堆为空，nums为数组
        self.heap = []
        if nums:
            self.build_heap(nums)

    def len_heap(self):  # 数组的长度，堆元素的个数
        return len(self.heap)

    def height(self):  # 堆的高度
        return math.ceil(math.log(len(self.heap)) / math.log(2))

    def is_leaf(self, i):  # 是否是叶子结点
        return i > int(math.ceil(len(self.heap) - 2) / 2.0)

    def parent(self, i):  # 父结点
        if i == 0:
            return -1
        elif i % 2 != 0:
            return (i - 1) / 2
        return (i - 2) / 2

    def leftchild(self, i):  # 左孩子
        return 2 * i + 1

    def rightchild(self, i):  # 右孩子
        return 2 * i + 2

    def heapify(self, i):  # 堆调整
        l = self.leftchild(i)
        r = self.rightchild(i)
        smallest = i
        if i < self.len_heap() and self.heap[l] < self.heap[smallest]:
            smallest = l
        elif r < self.len_heap() and self.heap[r] < self.heap[smallest]:
            smallest = r
        elif smallest != i:  # 交换
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)  # 递归查找最小值

    def build_heap(self, nums):  # 堆建立
        self.heap = nums[:]  # 数组元素
        last_leaf = self.parent(len(self.heap) - 1)
        print 'len:', len(self.heap)
        print 'last_leaf:', last_leaf  # 3,2,1,0 共四层
        for i in range(last_leaf, -1, -1):
            self.heapify(i)

    def heappush(self, x):  # 插入元素
        i = len(self.heap)  # i为heap的长度，也就是插入元素的位置，heap从0开始的
        self.heap.append(x)
        parent = self.parent(i)
        while parent != -1 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent(i)

    def heappop(self):  # 删除元素,每次只能删除堆顶元素
        if self.len_heap():
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            pop = self.heap.pop()
            self.heapify(0)
            return pop
        raise Exception('Heap is empty')


if __name__ == '__main__':
    minheap = minheap()
    nums = [15, 32, 3, 6, 27, 18, 65, 36, 28]
    minheap.build_heap(nums)
    print minheap.heappop()
