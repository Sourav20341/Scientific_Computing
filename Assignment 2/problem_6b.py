import numpy as np
from scipy.linalg import solve_triangular


def A(k):
    arr = np.zeros((3, 2))
    arr[0][0] = 1
    arr[0][1] = 1
    arr[1][0] = 10 ** (-k)
    arr[1][1] = 0
    arr[2][0] = 0
    arr[2][1] = 10 ** (-k)
    return arr


def b(k):
    arr = np.zeros((3, 1))
    arr[0][0] = -10 ** (-k)
    arr[1][0] = 1 + 10 ** (-k)
    arr[2][0] = 1 - 10 ** (-k)
    return arr


for i in range(6, 16):
    arrayA = A(i)
    arrayb = b(i)
    Q, R = np.linalg.qr(arrayA)
    arrayb = np.matmul(Q.T, arrayb)
    x = solve_triangular(R, arrayb)
    print("X for k = " + str(i) + " using QR factorization : " + str(x) + "\n")
