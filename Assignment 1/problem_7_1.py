import numpy as np

sum = 0
for i in range(1,5001):
  sum += 1/i
  if(i%100 == 0):
    print(sum - np.log(i))

print("Final Result : "+str(sum - np.log(5000)))