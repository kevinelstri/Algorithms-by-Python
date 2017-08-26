# coding:utf-8

from minheap import minheap


def heapsort(nums):
    h = minheap(nums)
    return [h.heappop() for i in range(h.len_heap())]


if __name__ == '__main__':
    nums = [15, 32, 3, 6, 27, 18, 65, 36, 28]
    print heapsort(nums)
