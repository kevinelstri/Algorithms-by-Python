# coding:utf-8


def max_heapify(seq, i, n):  # 堆调整
    l = 2 * i + 1
    r = 2 * i + 2

    if l <= n and seq[l] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r

    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)


def min_heapify(seq, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    if l <= n and r <= n and seq[l] <= seq[r]:
        smallest = seq[l]
        if smallest < seq[i]:
            seq[l], seq[i] = seq[i], seq[l]
    else:
        smallest = seq[r]
        if smallest < seq[i]:
            seq[r], seq[i] = seq[i], seq[r]


def max_build_heap(seq):  # 堆建立
    n = len(seq)
    for i in range(n / 2-1, -1, -1):
        max_heapify(seq, i, n)


def min_build_heap(seq):  # 堆建立
    n = len(seq)
    for i in range(0, n / 2):
        min_heapify(seq, i, n)


def max_sort(seq):
    max_build_heap(seq)
    # heap_size = len(seq) - 1
    # for x in range(heap_size, 0, -1):
    #     seq[0], seq[x] = seq[x], seq[0]
    #     heap_size = heap_size - 1
    #     max_heapify(seq, 0, heap_size)
    return seq


def min_sort(seq):
    min_build_heap(seq)
    # heap_size = len(seq) - 1
    # for x in range(heap_size, 0, -1):
    #     seq[0], seq[x] = seq[x], seq[0]
    #     heap_size = heap_size - 1
    #     min_heapify(seq, 0, heap_size)
    return seq


if __name__ == '__main__':
    seq = [15, 32, 3, 6, 27, 18, 65, 36, 28]
    # print seq
    print max_sort(seq)
    # print min_sort(seq)
