# coding:utf-8


# bubble sort:循环比较两个相邻位置之间的大小关系
def bubbleSort(num_list):
    L = len(num_list)
    while L > 1:
        for i in range(L-1):
            if num_list[i]>num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp
        L -= 1
    return num_list

if __name__ == "__main__":
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print bubbleSort(num_list)
