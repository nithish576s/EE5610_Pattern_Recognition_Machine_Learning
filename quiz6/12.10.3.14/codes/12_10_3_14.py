import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *


a1 = np.zeros((3,1))
b1 = np.random.rand(3,1)

print('a: ',a1)
print('b: ',b1)
print('inner product between a and b: ',a1.T @ b1)

print('Counter Example for Converse:\n')
a2 = np.array([[1],[-1]],ndmin=2)
b2 = np.array([[1],[1]],ndmin=2)
print('a: ',a2)
print('b: ',b2)
print('inner product between a and b: ',a2.T @ b2)

line_OA = line_gen(np.array([[0],[0]],ndmin=2),a2) 
line_OB = line_gen(np.array([[0],[0]],ndmin=2),b2)


plt.scatter(a2[0][0],a2[1][0])
plt.scatter(b2[0][0],b2[1][0])
plt.annotate('A(1,-1)',(a2[0][0],a2[1][0]))
plt.annotate('A(1,1)',(b2[0][0],b2[1][0]))

plt.plot(line_OA[0,:],line_OA[1,:])
plt.plot(line_OB[0,:],line_OB[1,:])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz6/12.10.3.14/figs/vector_plot.jpg")
plt.show()

 
