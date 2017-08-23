# coding:utf-8


# bubble sort: The number of bubble sort
def bubbleSort(num_list, number):
    L = len(num_list)
    num = 0
    while L > 1 and num <= number:
        for i in range(L - 1):
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp
            num += 1
    return num_list


if __name__ == '__main__':
    num_list1 = [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
    num_list2 = [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
    num_list3 = [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
    num_list4 = [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
    print bubbleSort(num_list1, 3)
    print bubbleSort(num_list2, 3)
    print bubbleSort(num_list3, 3)
    print bubbleSort(num_list4, 3)
