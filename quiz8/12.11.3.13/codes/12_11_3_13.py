import numpy as np

n1 = np.array([7,5,6])
n2 = np.array([3,-1,-10])

mat = np.array([n1,n2])

print(mat)
print('The rank of the matrix is: ',np.linalg.matrix_rank(mat))

print('The inner product between the normal vectors is: ',n1.T @ n2)

print('The angle between the two planes is: ',np.arccos((n1.T @ n2)/(np.linalg.norm(n1)*np.linalg.norm(n2))),'radians')

