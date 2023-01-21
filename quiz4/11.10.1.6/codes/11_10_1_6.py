import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')

from line.funcs import *


A = np.array([4,4])
B = np.array([3,5])
C = np.array([-1,-1])

#finding vector of the sides BA and CA
AB = B-A
AC = C-A
BC = C-B

#finding the angle of A of the triangle ABC
phi = np.arccos((np.dot(AB.T,AC))/(np.linalg.norm(AB)*np.linalg.norm(AC)))
print('angle A of triangle ABC is: ',(phi*180)/np.pi,'degrees')

#plotting the triangle
pnts_AB = line_gen(A,B)
pnts_BC = line_gen(B,C)
pnts_CA = line_gen(C,A)

#print(pnts_AB.shape)

plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])

plt.annotate('A',(A[0],A[1]))
plt.annotate('B',(B[0],B[1]))
plt.annotate('C',(C[0],C[1]))


plt.plot(pnts_AB[0,:],pnts_AB[1,:])
plt.plot(pnts_BC[0,:],pnts_BC[1,:])
plt.plot(pnts_CA[0,:],pnts_CA[1,:])

plt.xlim([-2,6])
plt.ylim([-2,6])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.savefig("triangle_plot.jpg")

plt.show()
