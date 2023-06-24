import numpy as np
import matplotlib.pyplot as plt
import math

def twonorm(r):
    val = 0
    for i in r:
        val += i**2
    return math.sqrt(val)

def Y(val):
    a1 = math.log(val) - math.log(1-val)
    return a1

A = np.zeros((50,2))
b = np.zeros((50,1))
t, y = np.loadtxt("hw2_data_ty.txt").T

for i in range(50):
    A[i][0] = 1
    A[i][1] = t[i]

for i in range(50):
    b[i] = Y(y[i])

ATA = np.matmul(A.T,A)
ATB = np.matmul(A.T,b)
x = np.linalg.solve(ATA,ATB)
r = b - np.matmul(A,x)
print("Residual Norm by normal equation  : " + str(twonorm(r)))

x1 = np.linalg.lstsq(A,b,rcond=None)
r1 = b - np.matmul(A,x1[0])
print("Residual Norm by np.linalg.lstsq : " + str(twonorm(r1)))

plt.figure()
plt.plot(t, y, 'bo', ms=2.5)
plt.grid(True)
YY = []
for i in t:
    up = math.exp(x[1]*i + x[0])
    down = 1+math.exp(x[1]*i + x[0])
    YY.append(up/down)
plt.plot(t,YY,'r',label = "Best fit line by normal equation with residual value " + str(twonorm(r)))
YY = []
for i in t:
    up = math.exp(x1[0][1]*i + x1[0][0])
    down = 1+math.exp(x1[0][1]*i + x1[0][0])
    YY.append(up/down)
plt.plot(t,YY,'b',linestyle='dashed',label = "Best fit line by np.lingalg.lstsq with residual value " + str(twonorm(r1)))
plt.xlabel("$t_i$", fontsize=14)
plt.ylabel("$f(t_i)$", fontsize=14)
plt.legend()
plt.gcf().tight_layout()
plt.show()