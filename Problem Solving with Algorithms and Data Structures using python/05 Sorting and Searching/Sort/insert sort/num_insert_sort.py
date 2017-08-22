# coding:utf-8


# insert sort: the number of insert sort
def numInsertSort(num_list, number):
    L = 1
    leng = len(num_list)
    num = 1
    while L < leng and num <= number:
        index = L
        while (index >= 1) and (num_list[index] < num_list[index - 1]):
            temp = num_list[index]
            num_list[index] = num_list[index - 1]
            num_list[index - 1] = temp
            index -= 1
        num += 1
        L += 1
    return num_list


if __name__ == '__main__':
    num_list1 = [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
    num_list2 = [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]
    num_list3 = [4, 5, 15, 18, 12, 19, 14, 10, 8, 20]
    num_list4 = [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]
    print numInsertSort(num_list1, 2)
    print numInsertSort(num_list2, 2)
    print numInsertSort(num_list3, 2)
    print numInsertSort(num_list4, 2)
