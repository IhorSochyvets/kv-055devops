#define a function diagonalReverse() that takes matrix and returns diagonal-reversed one:
#1 2 3         1 4 7
#4 5 6 returns 2 5 8
#7 8 9         3 6 9

N = 3

def showMatrix(array):
    i = 0
    j = N
    for i in range(N):
        for j in range( N):
            print( array[i][j],end="  ")
        print()

def reverseDiagonal(array):
    array_new = [[ 0, 0,  0],
                   [0, 0,  0],
                   [0, 0, 0]]
    for j in range(N):
        for i in range(N):
    #        print(array[i][j])
            array_new[i][j] = array[j][i]


    # Print new matrix after rever

    for i in range(N):
        for j in range( N):
            print( array_new[i][j],end="  ")
        print()

matrix = [[ 1, 2,  3],
            [4, 5,  6],
            [7, 8, 9]]
print('Original matrix:')
showMatrix(matrix)
print('Reversed matrix:')
reverseDiagonal(matrix)
