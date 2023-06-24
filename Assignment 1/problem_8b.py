# -*- coding: utf-8 -*-
"""problem_8b

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYFpYvHIw0Qkj4oWdoOeAd5HG2Jz3BsO
"""

# Gaussian Elimination with partial pivoting
import numpy as np
def gaussian_with_partial(A,b):
  m = A.shape
  n = m[0]
  l = np.zeros(n)
  s = np.zeros(n)
  for i in range(n):
    l[i] = i
    smax = 0
    for j in range(n):
      smax = max(smax,abs(A[i][j]))
    s[i] = smax

  for k in range(n-1):
    j = k
    rmax = 0
    for i in range(k,n):
      r = abs(A[int(l[i])][k]/s[int(l[i])])
      if r > rmax:
        rmax = r
        j = i
    ltemp = l[k]
    l[k] = l[j]
    l[j] = ltemp
    for i in range(k+1,n):
      amult = A[int(l[i])][k]/A[int(l[k])][k]
      A[int(l[i])][k] = amult
      for j in range(k+1,n):
        A[int(l[i])][j] = A[int(l[i])][j] - amult*A[int(l[k])][j]
  for k in range(0,n-1):
    for i in range(k+1,n):
      b[int(l[i])] = b[int(l[i])] - A[int(l[i])][k]*b[int(l[k])]

  x = np.zeros(n)
  x[n-1] = b[int(l[n-1])]/A[int(l[n-1])][n-1]
  i = n-2
  while i >= 0:
    sum =  b[int(l[i])]
    for j in range(i + 1,n):
      sum = sum - A[int(l[i])][j] * x[j]
    x[i] = round(sum/A[int(l[i])][i],2)
    i-=1
  return x