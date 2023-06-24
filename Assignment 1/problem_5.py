import numpy as np

for j in range(0,21):
  x = np.pi/4 + 2*np.pi*(10**j)
  yabs = abs(np.tan(x)-1)
  conditionRel = abs((x * ((1/np.cos(x))**2))/np.tan(x))
  conditionAbs = abs(((1/np.cos(x))**2))
  print("(x, tan(x), Abs. Forward Error, Abs. Backward Error, Relative Condition Number) = (%1.16f, %1.16f, %1.16f, %1.16f, %1.16f)"%(x, np.tan(x),yabs,yabs/conditionAbs,conditionRel))