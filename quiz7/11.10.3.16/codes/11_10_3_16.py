import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *


#Let us take theta=30
n1 = np.array([np.cos(np.pi/6), np.sin(np.pi/6)])
n2 = np.array([1/np.cos(np.pi/6), 1/np.sin(np.pi/6)])

#Let us take k=4
k = 4
c1 = k*np.cos(np.pi/3)
c2 = k

dir_vec_1 = norm_vec(0,n1)
dir_vec_2 = norm_vec(0,n2)

orig = np.array([0,0])

FOP_1 = perp_foot(n1,c1,orig)
FOP_2 = perp_foot(n2,c2,orig)

p = np.linalg.norm(FOP_1)
q = np.linalg.norm(FOP_2)

print('LHS: ',p**2+4*q**2)

print('RHS: ',k**2)

line_1 = line_dir_pt(dir_vec_1,FOP_1,-5,5) 
line_2 = line_dir_pt(dir_vec_2,FOP_2,-3,3)

normal_1 = line_gen(np.array([0,0]),FOP_1)
normal_2 = line_gen(np.array([0,0]),FOP_2)

plt.scatter(FOP_1[0],FOP_1[1])
plt.scatter(FOP_2[0],FOP_2[1])


plt.plot(line_1[0,:],line_1[1,:])
plt.plot(line_2[0,:],line_2[1,:])
plt.plot(normal_1[0,:],normal_1[1,:])
plt.plot(normal_2[0,:],normal_2[1,:])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.axis('equal')
plt.legend(['line 1','line 2','normal 1','normal 2'])
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz7/11.10.3.16/figs/line_plot.jpg")
plt.show()

