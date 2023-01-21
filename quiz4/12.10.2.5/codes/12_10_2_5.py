import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/nithish/Downloads/training-main/math/codes/CoordGeo/')

from line.funcs import *

#Initial point
I = np.array([2,1])

#Terminal point
F = np.array([-5,7])

#vector
V = F-I

scalar_comp1 = V[0]
scalar_comp2 = V[1]
vector_comp = V

print('Scalar Components: ',scalar_comp1,' ',scalar_comp2)
print('Vector Components: ',vector_comp[0],'i ',vector_comp[1],'j ')

#plotting
line_pnts = line_gen(I,F)

plt.plot(line_pnts[0,:],line_pnts[1,:])

plt.scatter(I[0],I[1])
plt.scatter(F[0],F[1])

plt.annotate('I(2,1)',(I[0],I[1]))
plt.annotate('F(-5,7)',(F[0],F[1]))

plt.savefig("./fig/line_plot.jpg")

plt.show()
