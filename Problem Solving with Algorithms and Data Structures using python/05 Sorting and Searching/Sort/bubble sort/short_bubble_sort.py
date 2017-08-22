# coding:utf-8


# bubble sort : if the list is order,stop to compare the number
def shortBubbleSort(num_list):
    judge = True
    L = len(num_list)
    num = 0
    while L > 1 and judge:
        judge = False
        for i in range(L - 1):
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp
            num += 1
        L -= 1
    print num
    return num_list


if __name__ == '__main__':
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print shortBubbleSort(num_list)
