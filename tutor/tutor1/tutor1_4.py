from operator import index, indexOf


A = [[1, 2, 3, 4], [5, 6, 7, 8], [2, 3, 9, 3]]

for i in range(len(A)):
    for j in range(len(A[i])):
        if (i!=0 and i != len(A) - 1 ) and (j!=0 and j != len(A[i]) - 1):
            print(" ", end='\t')
        else:
            print(A[i][j], end='\t')
    print('')


# i is not 0 and i is not 2
# j is not 0 and j is not 3

# x = [1,2,3,4]
# y = x.copy()

# print(x is y)