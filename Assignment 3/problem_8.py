import numpy as np
import math
import matplotlib.pyplot as plt

def RayleighQuotient(A,x):
  prevsigma = 0
  rate = 0
  eigenval = 11
  preverror = 0
  C = 1
  tolerance = 1e-15
  ratearr = []
  for i in range(1000):
    sigma = np.matmul(np.matmul(x.T,A),x)/np.matmul(x.T,x)
    B = A-(sigma*np.identity(A.shape[0]))
    y = np.linalg.solve(B,x)
    a = abs(y).max(axis = 0)
    x = y/a
    error = eigenval-sigma
    rate = math.log(abs(error)+tolerance,C*abs(preverror)+tolerance)
    ratearr.append(rate)
    if(prevsigma == sigma):
      break
    prevsigma = sigma
    preverror = error
  return rate,x,prevsigma,ratearr

A = np.array([[2,3,2],[10,3,4],[3,6,1]])
x = np.array([[2,2,1]])
x = x.T
rate,eigenvector,eigenvalue,ratearr = RayleighQuotient(A,x)
print("Rate :- ",rate)
print("Eigenvector :- ")
print(eigenvector)
print("Eigenvalue :- ",eigenvalue)
plt.plot(ratearr)