# coding:utf-8

'''
顺时针打印矩阵
'''


def printMatrix(matrix, m, n):
    row = len(matrix) - m
    col = len(matrix[0]) - n
    x = m

    # 从左到有
    for j in range(n, col):
        print matrix[x][j]
    y = j
    # print 'j:',j
    # 从上到下
    for i in range(1, row):
        print matrix[i][y]
    x = i

    # print 'i:',i
    # 从右到左
    for j in range(col - 2, n - 1, -1):
        print matrix[x][j]
    y = j
    # 从下到上
    for i in range(row - 2, m, -1):
        print matrix[i][y]

    print '---------------------------'


def Matrix(matrix):
    x = min(len(matrix), len(matrix[0]))
    if x % 2 == 0:
        for i in range(x):
            printMatrix(matrix, i, i)
    else:
        for i in range(x + 1):
            printMatrix(matrix, i, i)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5],
              [5, 6, 7, 8, 9],
              [9, 10, 11, 12, 13],
              [13, 14, 15, 16, 17],
              [17, 18, 19, 20, 21]]
    m1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    m2 = [[1, 2, 3, 4]]
    m3 = [[1,
           2,
           3,
           4]]

    # printMatrix(matrix, i, j)
    # printMatrix(m1, i, j)
    # printMatrix(m2, i, j)
    # printMatrix(m3, i, j)
    Matrix(matrix)
