import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *
from conics.funcs import *


centre = np.array([0,0])

inner_circle = circ_gen(centre,3)
outter_circle = circ_gen(centre,5)

A = np.array([1-np.sqrt(23/2),-1-np.sqrt(23/2)])
B = np.array([1-np.sqrt(7/2),-1-np.sqrt(7/2)])
C = np.array([1+np.sqrt(7/2),-1+np.sqrt(7/2)])
D = np.array([1+np.sqrt(23/2),-1+np.sqrt(23/2)])

print('A: ',A)
print('B: ',B)
print('C: ',C)
print('D: ',D)

AB = np.linalg.norm(A-B)
CD = np.linalg.norm(C-D)

print('Length of AB is:',AB)
print('Length of CD is:',CD)

if AB==CD:
    print('AB and CD are of equal length')


pnt = np.array([0,-2])
dir_vec = np.array([1,1])
line = line_dir_pt(dir_vec,pnt,-5,6)

plt.plot(line[0,:],line[1,:])
plt.plot(inner_circle[0,:],inner_circle[1,:])
plt.plot(outter_circle[0,:],outter_circle[1,:])

plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])
plt.scatter(D[0],D[1])
plt.scatter(centre[0],centre[1])

plt.annotate('A',A)
plt.annotate('B',B)
plt.annotate('C',C)
plt.annotate('D',D)
plt.annotate('O',centre)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-6,6])
plt.ylim([-8,8])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz9/9.10.4.4/figs/plot.jpg")
plt.show()
