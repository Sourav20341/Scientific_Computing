# -*- coding: utf-8 -*-
"""problem_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17vNWFyeB9MLdeAxASScT09ptLx6CvsqS
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def datapoints(n):
  y = None
  if(n == 11):
    y = [-1/5,-2/5,-3/5,-4/5,-1,0,1/5,2/5,3/5,4/5,1]
  
  if(n == 21):
    y =  [-1/10,-2/10,-3/10,-4/10,-5/10,-6/10,-7/10,-8/10,-9/10,-1,0,1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,1]
  y.sort()
  return y

def runge_function(t):
  y = 1 + 25*t*t
  return 1/y

def V_x(n,x_arr):
  V = []
  for i in range(len(x_arr)):
    arr = []
    for j in range(n):
      arr.append(math.pow(float(x_arr[i]),j))
    V.append(arr)
  V = np.array(V)
  return V

def poly_interpolate(n,x_arr,y_arr):
  V = V_x(n,x_arr)
  b = np.linalg.solve(V,y_arr)
  return V,b

def compute(x,w):
  len = w.shape[0]
  val = 0
  for i in range(0,len):
    x_coeff = 1
    for j in range(0,i):
      x_coeff = x*x_coeff
    val += w[i]*x_coeff
  return val

# 11 Polynomial
x_11 = datapoints(11)
y_11 = []
for i in x_11:
  y_11.append(runge_function(i))

V_11,b_11 = poly_interpolate(11,x_11,y_11)
y_b_11 = np.matmul(V_11,b_11)
T = np.linspace(-1, 1, 100)
f_at_T = np.array([runge_function(t_) for t_ in T])
f_at_computed = np.array([compute(t_,b_11) for t_ in T])
plt.plot(T, f_at_computed)
plt.grid(True)
plt.xlabel('t', fontsize=12)
plt.ylabel('f(t)', fontsize=12)
plt.title('Plot of Polynomial function', fontsize=14)

# 21 Polynomial
x_21 = datapoints(21)
y_21 = []
for i in x_21:
  y_21.append(runge_function(i))

V_21,b_21 = poly_interpolate(21,x_21,y_21)
y_b_21 = np.matmul(V_21,b_21)       

T = np.linspace(-1, 1, 100)
f_at_T = np.array([runge_function(t_) for t_ in T])
f_at_computed = np.array([compute(t_,b_21) for t_ in T])
plt.plot(T, f_at_computed)
plt.grid(True)
plt.xlabel('t', fontsize=12)
plt.ylabel('f(t)', fontsize=12)
plt.title('Plot of Polynomial function', fontsize=14)