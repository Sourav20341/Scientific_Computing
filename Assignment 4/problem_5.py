# -*- coding: utf-8 -*-
"""problem_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z6tglebQTlfE1LaP4L2KKOGAvbDpOIg2
"""

import math
import seaborn as sns

def f(x):
  y = math.exp((-math.sin(x*x*x)/4))
  return y;

def actual_derivative(x):
  y = (-3/4) * (x*x) * math.cos(x*x*x) * f(x)
  return y

def computed_derivative(x,h):
  y = f(x+h) - f(x)
  y = y/h
  return y

def relative_error(x,x0):
  y = abs(x-x0)
  return y

x_arr = []
y_arr = []
y_true = actual_derivative(1)
for i in range(1,16):
  y_computed = computed_derivative(1,math.pow(10,-i))
  x_arr.append(-i)
  print("Absolute Error for h = 10^" + str(-i) + " is : ",relative_error(y_computed,y_true))
  #print("Absolute log Error for h = 10^" + str(-i) + " is : ",math.log(relative_error(y_computed,y_true)))
  y_arr.append(math.log(relative_error(y_computed,y_true)))

ax = sns.scatterplot(x_arr,y_arr)
ax.set(title = "Log-Log Curve",xlabel = "log(h) value",ylabel = "Log(Absolute Error)")