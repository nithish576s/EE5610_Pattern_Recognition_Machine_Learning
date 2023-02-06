import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *


a = np.array([3,0])
b = np.array([1/3,1/3])
print('a: ',a)
print('b: ',b)

print('norm of a: ',np.linalg.norm(a))
print('norm of b: ',np.linalg.norm(b))

c = np.cross(a,b)

print('cross product of a and b: ',c)
print('norm of cross product of a and b: ',np.linalg.norm(c))

phi = np.arccos((a.T @ b)/(np.linalg.norm(a)*np.linalg.norm(b)))



line_OA = line_gen(np.array([0,0]),a) 
line_OB = line_gen(np.array([0,0]),b)


plt.scatter(a[0],a[1])
plt.scatter(b[0],b[1])
plt.annotate('A(3,0)',(a[0],a[1]))
plt.annotate('B(1/3,1/3)',(b[0],b[1]))

plt.plot(line_OA[0,:],line_OA[1,:])
plt.plot(line_OB[0,:],line_OB[1,:])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz6/12.10.4.11/figs/vector_plot.jpg")
plt.show()

