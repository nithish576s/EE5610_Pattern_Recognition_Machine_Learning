import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')

from line.funcs import *

#vector a
a = np.array([1,2])

#vector b
b = np.array([3,8])

#print('a: ',np.linalg.norm(a))
#print('b: ',np.linalg.norm(b))

#vector v = |a|b+|b|a
v = np.linalg.norm(b)*a+np.linalg.norm(a)*b

#vector u = |a|b-|b|a
u = np.linalg.norm(a)*b-np.linalg.norm(b)*a

phi = (np.arccos((np.dot(v.T,u))/(np.linalg.norm(v)*np.linalg.norm(u)))*180)/np.pi

print('angle between vectors v and u is: ',phi)
print('hence the two vectors are perpendicular')

#plotting the vectors
y_intercept = np.array([0,0])

dir_u = u/u[0]
dir_v = v/v[0]

print(dir_u)
print(dir_v)

line_u = line_dir_pt(dir_u,y_intercept,-3,3)
line_v = line_dir_pt(dir_v,y_intercept,-3,3)

print('line_u ',line_u)
print('line_v ',line_v)
plt.plot(line_u[0,:],line_u[1,:])
plt.plot(line_v[0,:],line_v[1,:])

plt.xlim([-8,8])
plt.ylim([-8,8])

plt.savefig("./fig/line_plot.jpg")

plt.show()
