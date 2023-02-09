import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *


n1 = np.array([np.cos(np.pi/6), np.sin(np.pi/6)])

orig = np.array([0,0])

d = 5

c1 = np.abs(n1.T@np.zeros_like(n1) - d)/np.linalg.norm(n1)
c2 = -np.abs(n1.T@np.zeros_like(n1) - d)/np.linalg.norm(n1)

print('normal vector of line 1:\n',n1)
print('c: ',c1)
print('normal vector of line 2:\n',n1)
print('c: ',c2)

dir_vec1 =  norm_vec(orig,n1)
dir_vec2 =  norm_vec(orig,n1)

line1 = line_dir_pt(dir_vec1,d*n1,-5,5)
normal1 = line_gen(np.array([0,0]),d*n1)
plt.scatter(d*n1[0],d*n1[1])

line2 = line_dir_pt(dir_vec2,-1*d*n1,-5,5)
normal2 = line_gen(np.array([0,0]),-1*d*n1)
plt.scatter(-1*d*n1[0],-1*d*n1[1])


plt.plot(line1[0,:],line1[1,:],label="line")
plt.plot(normal1[0,:],normal1[1,:],label="normal")
plt.plot(line2[0,:],line2[1,:],label="line")
plt.plot(normal2[0,:],normal2[1,:],label="normal")

plt.legend(['line 1','normal 1','line 2','normal 2'])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz7/11.10.2.8/figs/line_plot.jpg")
plt.show()

