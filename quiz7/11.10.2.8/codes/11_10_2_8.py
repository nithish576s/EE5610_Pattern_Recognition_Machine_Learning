import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *


n = np.array([np.cos(np.pi/6), np.sin(np.pi/6)])

orig = np.array([0,0])

d = 5

c = np.abs(n.T@np.zeros_like(n) - d)/np.linalg.norm(n)

print('normal vector of line:\n',n)
print('c: ',c)

dir_vec =  norm_vec(orig,n)

line = line_dir_pt(dir_vec,d*n,-3,3)
normal = line_gen(np.array([0,0]),d*n)
plt.scatter(d*n[0],d*n[1])

plt.annotate('Feet of perpendicular',(d*n[0],d*n[1]))


plt.plot(line[0,:],line[1,:],label="line")
plt.plot(normal[0,:],normal[1,:],label="normal")
plt.legend(['line','normal'])


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz7/11.10.2.8/figs/line_plot.jpg")
plt.show()

