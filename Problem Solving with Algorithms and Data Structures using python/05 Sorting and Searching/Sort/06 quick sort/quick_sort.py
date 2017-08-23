# coding:utf-8


# quick sort
def quickSort(num_list):
    quickSortHelper(num_list, 0, len(num_list) - 1)


def quickSortHelper(num_list, first, last):
    if first < last:
        split_point = partition(num_list, first, last)
        quickSortHelper(num_list, first, split_point - 1)
        quickSortHelper(num_list, split_point + 1, last)


def partition(num_list, first, last):
    pivot_value = num_list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and num_list[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and num_list[right_mark] >= pivot_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = num_list[left_mark]
            num_list[left_mark] = num_list[right_mark]
            num_list[right_mark] = temp

    temp = num_list[first]
    num_list[first] = num_list[right_mark]
    num_list[right_mark] = temp

    return right_mark


if __name__ == '__main__':
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print quickSort(num_list)
