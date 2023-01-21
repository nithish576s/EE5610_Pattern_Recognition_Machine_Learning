import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo')

from line.funcs import *

#point
x0 = np.array([-4,3])

#slope
m = 1/2

#direction vector
m_l = np.array([1,m])

#normal vector
o_mat = np.array([[0,-1],[1,0]])
n_l = np.dot(o_mat,m_l)

print('direction_vector: ',m_l)
print('normal_vector: ',n_l)
print('point: ',x0)


#y-intercept
y_0 = x0 - x0[0]*m_l
print(y_0)

line_pts = line_dir_pt(m_l,y_0,-5,5)

plt.plot(line_pts[0,:],line_pts[1,:])

plt.scatter(x0[0],x0[1])
plt.scatter(y_0[0],y_0[1])

plt.annotate('X0(-4,3)',(x0[0],x0[1]))
plt.annotate('Y-intercept(0,5)',(y_0[0],y_0[1]))

plt.savefig("./fig/line_plot.jpg")

plt.show()
