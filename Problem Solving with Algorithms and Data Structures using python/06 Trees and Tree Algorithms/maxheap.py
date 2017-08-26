# coding:utf-8

from minheap import minheap

class maxheap(minheap):

    MAX_HEAP = True

    def heapify(self, i):
        l = self.leftchild(i)
        r = self.rightchild(i)
        largest = i
        if l < self.len_heap() and self.heap[i] > self.heap[largest]:
            largest = l
        elif r < self.len_heap() and self.heap[i]>self.heap[largest]:
            largest = r
        elif largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def heappush(self, x):
        i = len(self.heap)
        self.heap.append(x)
        parent = self.parent(i)
        while parent != -1 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.[parent], self.heap[i]  # 交换
            i = parent
            parent = self.parent(i)




