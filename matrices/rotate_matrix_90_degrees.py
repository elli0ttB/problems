# rotata a square matrix A by 90 degrees in-place
from copy import deepcopy

def rotate_90(A):
    # end = len(A) - 1
    for j in range(int(len(A)/2)):
        for i in range(j, len(A) - j - 1):
            L,M = j,i
            for k in range(3):
                L, M = M, (len(A) - 1 - L)
                A[j][i], A[L][M] = A[L][M], A[j][i]

