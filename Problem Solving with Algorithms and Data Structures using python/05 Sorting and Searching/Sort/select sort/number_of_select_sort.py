# coding:utf-8


# select sort: the number of select sort
def numSelectSort(num_list, number):
    L = -1
    leng = len(num_list)
    num = 1
    while L > -leng and num <= number:
        max_num = max(num_list[:L])
        x = num_list.index(max_num)
        if num_list[x] > num_list[L]:
            temp = num_list[x]
            num_list[x] = num_list[L]
            num_list[L] = temp
        L -= 1
        num += 1
    return num_list


if __name__ == '__main__':
    num_list1 = [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
    num_list2 = [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
    num_list3 = [11, 7, 12, 13, 1, 6, 8, 18, 19, 20]
    num_list4 = [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
    print numSelectSort(num_list1, 3)
    print numSelectSort(num_list2, 3)
    print numSelectSort(num_list3, 3)
    print numSelectSort(num_list4, 3)
