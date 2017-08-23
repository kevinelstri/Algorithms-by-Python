# coding:utf-8


# merge sort
def mergeSort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) / 2
        left = num_list[:mid]
        right = num_list[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1
    print num_list


if __name__ == '__main__':
    num_list = [54, 26, 93, 2, 17, 77, 31, 44, 55, 20, 12]
    mergeSort(num_list)
