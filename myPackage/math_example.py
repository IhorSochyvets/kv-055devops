def myFun(x):
    if (type(x) != int):
        raise TypeError
    a = x + 2
    #....much logic
    print(a)
    return a


# def diagonalReverse(_list):
#     return [list(i) for i in zip(*_list)]


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(diagonalReverse(matrix))
