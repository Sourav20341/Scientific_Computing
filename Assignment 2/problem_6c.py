import numpy as np
from scipy.linalg import solve


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
    XtX = np.matmul(arrayA.T, arrayA)
    arrayb = np.matmul(arrayA.T, arrayb)
    if np.linalg.det(XtX) == 0:
        print("XTX becomes singular")
        continue
    x = solve(XtX, arrayb)
    print("X for k = " + str(i) + " using normal equation : " + str(x) + "\n")
