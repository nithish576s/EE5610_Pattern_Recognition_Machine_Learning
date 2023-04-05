import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

m = np.array([4,3])
c = 12
P1 = np.array([0,32/3])

x1 = cp.Variable(2)

constraints1 = [m @ x1==c]

objective1 = cp.Minimize(cp.norm(x1-P1))

problem1 = cp.Problem(objective1,constraints1)

result1 = problem1.solve()

print('length of the perpendicular from (0,32/3) to the line: ',result1)

print('feet of perpendicular from (0,32/3) to the line: ',x1.value)


P2 = np.array([0,-8/3])

x2 = cp.Variable(2)

constraints2 = [m @ x2==c]

objective2 = cp.Minimize(cp.norm(x2-P2))

problem2 = cp.Problem(objective2,constraints2)

result2 = problem2.solve()

print('length of the perpendicular from (0,-8/3) to the line: ',result2)

print('feet of perpendicular from (0,-8/3) to the line: ',x2.value)


