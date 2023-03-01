import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')
from line.funcs import *
from conics.funcs import *


centre = np.array([0,0])

circle = circ_gen(centre,1)

A = np.array([np.cos(2*np.pi/3),np.sin(2*np.pi/3)])
C = np.array([np.cos(4*np.pi/3),np.sin(4*np.pi/3)])
D = np.array([np.cos(np.pi/6),np.sin(np.pi/6)])
E = np.array([np.cos(-np.pi/6),np.sin(-np.pi/6)])
B = np.array([np.sqrt(3)+1,0])

print('A: ',A)
print('C: ',C)
print('D: ',D)
print('E: ',E)
print('B: ',B)

AD = D-A
CE = E-C



angle_ABC = np.arccos((AD.T @ CE)/(np.linalg.norm(AD)*np.linalg.norm(CE)))*180/np.pi
angle_AOC = np.arccos((A.T @ C)/(np.linalg.norm(A)*np.linalg.norm(C)))*180/np.pi
angle_DOE = np.arccos((D.T @ E)/(np.linalg.norm(D)*np.linalg.norm(E)))*180/np.pi



print('angle ABC: ',angle_ABC,'degrees')
print('half of the difference of angles AOC and DOE is: ',(angle_AOC-angle_DOE)/2,'degrees')


line_AB = line_gen(A,B)
line_BC = line_gen(C,B)
line_AO = line_gen(A,centre)
line_CO = line_gen(C,centre)
line_DO = line_gen(D,centre)
line_EO = line_gen(E,centre)
line_AC = line_gen(A,C)
line_DE = line_gen(D,E)


plt.plot(circle[0,:],circle[1,:])
plt.plot(line_AB[0,:],line_AB[1,:])
plt.plot(line_BC[0,:],line_BC[1,:])
plt.plot(line_AO[0,:],line_AO[1,:])
plt.plot(line_DO[0,:],line_DO[1,:])
plt.plot(line_CO[0,:],line_CO[1,:])
plt.plot(line_EO[0,:],line_EO[1,:])
plt.plot(line_AC[0,:],line_AC[1,:])
plt.plot(line_DE[0,:],line_DE[1,:])

plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])
plt.scatter(D[0],D[1])
plt.scatter(E[0],E[1])
plt.scatter(centre[0],centre[1])

plt.annotate('A',A)
plt.annotate('B',B)
plt.annotate('C',C)
plt.annotate('D',D)
plt.annotate('E',E)
plt.annotate('O',centre)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([-6,6])
plt.ylim([-6,6])
plt.axis('equal')
plt.grid(visible='True',axis='both')
plt.savefig("/home/nithish/Documents/EE5610_Pattern_Recognition_Machine_Learning/quiz12/9.10.6.4/figs/plot.jpg")
plt.show()
