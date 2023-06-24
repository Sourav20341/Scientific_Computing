import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

x_noisy1 = np.loadtxt("hw2_data_denoising.txt",dtype = str)
x_noisy1[0] = "-1.0814120288205518e-02"
x_noisy = []
for i in x_noisy1:
    x_noisy.append(float(i))
x_noisy = np.array(x_noisy)
plt.figure()
plt.plot(np.arange(1, 1 + len(x_noisy)), x_noisy,
color=(0.5, 0.5, 0.5), label="Noisy Signal")

plt.xlabel("$n$", fontsize=14)
plt.ylabel("$x_{noisy}$", fontsize=14)
plt.legend(loc="best")
plt.gcf().tight_layout()
plt.show()

arr = [1,100,10000]

D = np.zeros((999,1000))
for i in range(999):
    for j in range(1000):
        if(i == j):
            D[i][j] = -1
            D[i][j+1] = 1

DTD = np.matmul(D.T,D)
for i in arr:
    lambdaDT = i*DTD
    A = np.identity(1000)+lambdaDT
    x = linalg.solve(A, x_noisy)
    plt.figure()
    plt.plot(np.arange(1, 1 + len(x)), x,color=(0.5, 0.5, 0.5), label="Noisy Signal for lambda = "+str(i))
    plt.xlabel("$n$", fontsize=14)
    plt.ylabel("$x_{noisy}$", fontsize=14)
    plt.legend(loc="best")
    plt.gcf().tight_layout()

plt.show()