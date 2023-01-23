import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')

from line.funcs import *

#the direction vector of y axis
m_y = np.array([0,1])

#finding the slope of the line from the quadratic equation(m/sqrt(m^2+1)=sqrt(3)/2)
m = np.sqrt(3)

#direction vector of the line
m_l = np.array([1,m])

#finding the angle between y-axis and the line
phi = (180*np.arccos(np.dot(m_y.T,m_l)/(np.linalg.norm(m_y)*np.linalg.norm(m_l))))/np.pi

print('the angle between the line and the y axis is: ',phi,' degrees')

#Let us take a line that has the given slope and y intercept 1 and plot it
y_intercept = np.array([0,1])

line_pnts = line_dir_pt(m_l,y_intercept,-3,3)
y_axis_pnts = np.zeros((2,10))
y_axis_pnts[1,:] = np.linspace(-5,5,10)

plt.plot(line_pnts[0,:],line_pnts[1,:])
plt.plot(y_axis_pnts[0,:],y_axis_pnts[1,:])

plt.legend(['line with slope sqrt(3)','y-axis'])

plt.xlim(-3,3)
plt.ylim(-5,5)

plt.savefig('/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz4/11.10.1.7/figs/line_plot.jpg')

plt.show()
