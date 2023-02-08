import numpy as np

#direction vector
m = np.array([-18,12,-4])
print('direction vector of the line is: \n',m)


#direction vector of X,Y and Z axis
e_1 = np.array([1,0,0])
e_2 = np.array([0,1,0])
e_3 = np.array([0,0,1])

E = np.array([[e_1.T],[e_2.T],[e_3.T]])

dir_cos = (E @ m)/np.linalg.norm(m)

print('direction cosine of the line is: \n',dir_cos)

