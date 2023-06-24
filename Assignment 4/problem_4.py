# -*- coding: utf-8 -*-
"""problem_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S2zmB_huWhI2KMmIsVhOsZEg0CveTYIE
"""

import math

def f(x):
  y = (100/x) * math.sin(10/x)
  return y

def CGQ(a,b,n):
  h = (b-a)/n
  sum = 0;
  i = 1;
  while(i < int(n/2)+1):
    x1 = a+2*(i-1)*h
    x2 = a+2*i*h
    t1 = ((x2-x1)*(1/math.pow(3,0.5))+x1+x2)/2
    t2 = ((x2-x1)*(-1/math.pow(3,0.5))+x1+x2)/2
    sum += ((x2-x1)/2) * (f(t2) + f(t1))
    i += 1
  return sum;

def relative_error(computed,actual):
  h = computed-actual
  h = h/actual
  return abs(h)


actual_val = -18.79829683678703
for i in range(2,66,2):
  result = CGQ(1,3,i)
  print("For n = ",i," Computed Value : ",result," Relative Error : ",relative_error(result,actual_val))