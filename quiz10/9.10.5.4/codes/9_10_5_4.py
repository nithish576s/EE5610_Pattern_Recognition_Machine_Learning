import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *
from conics.funcs import *


centre = np.array([0,0])

circle = circ_gen(centre,1)

A = np.array([np.cos(222*np.pi/180),-np.sin(222*np.pi/180)])
B = np.array([np.cos(160*np.pi/180),-np.sin(160*np.pi/180)])
C = np.array([1,0])
D = np.array([0,1])

print('A: ',A)
print('B: ',B)
print('C: ',C)
print('D: ',D)

BA = A-B
BC = C-B
CB = B-C
CA = A-C
DB = B-D
DC = C-D

angle_ABC = np.arccos((BA.T @ BC)/(np.linalg.norm(BA)*np.linalg.norm(BC)))*180/np.pi
angle_ACB = np.arccos((CB.T @ CA)/(np.linalg.norm(CB)*np.linalg.norm(CA)))*180/np.pi
angle_BDC = np.arccos((DB.T @ DC)/(np.linalg.norm(DB)*np.linalg.norm(DC)))*180/np.pi

print('angle ABC: ',angle_ABC,'degrees')
print('angle ACB: ',angle_ACB,'degrees')
print('angle BDC: ',angle_BDC,'degrees')


line_AB = line_gen(A,B)
line_BC = line_gen(B,C)
line_AC = line_gen(A,C)
line_DB = line_gen(D,B)
line_DC = line_gen(D,C)

plt.plot(circle[0,:],circle[1,:])
plt.plot(line_AB[0,:],line_AB[1,:])
plt.plot(line_BC[0,:],line_BC[1,:])
plt.plot(line_AC[0,:],line_AC[1,:])
plt.plot(line_DB[0,:],line_DB[1,:])
plt.plot(line_DC[0,:],line_DC[1,:])

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
plt.ylim([-6,6])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz10/9.10.5.4/figs/plot.jpg")
plt.show()
