# coding:utf-8


# shell sort
def shellSort(num_list):
    sublist_count = len(num_list) / 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(num_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", num_list)
        sublist_count /= 2


def gap_insertion_sort(num_list, start, gap):
    for i in range(start + gap, len(num_list), gap):
        current_value = num_list[i]
        position = i
        while position >= gap and num_list[position - gap] > current_value:
            num_list[position] = num_list[position - gap]
            position -= gap
        num_list[position] = current_value


if __name__ == '__main__':
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(num_list)
