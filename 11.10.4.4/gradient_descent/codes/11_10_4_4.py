import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/root/training/math/codes/CoordGeo/')
from line.funcs import *

m = np.array([4,3])
c = 12
P1 = np.array([0,32/3])

def function1(x):
    return 25*(x**2)+(160/3)*x+(400/9)

def grad1(x):
    return 50*x+(160/3)

def function2(x):
    return 25*(x**2)-(160/3)*x+(400/9)

def grad2(x):
    return 50*x-(160/3)

x = np.linspace(-5,5,1000)
y1 = function1(x)
plt.plot(x,y1)

alpha = 0.01
lambda_0 =1
eps = 1e-7
count = 0
N = 100000
lambda_n = lambda_0

while count<N and np.abs(alpha*grad1(lambda_n))>eps:
    nxt = lambda_n - alpha*grad1(lambda_n)
    count += 1
    new_coord = np.array([nxt,function1(nxt)])
    curr_coord = np.array([lambda_n,function1(lambda_n)])
    L = line_gen(curr_coord,new_coord)
    plt.plot(L[0],L[1])
    plt.plot(curr_coord[0],curr_coord[1],'k.')
    plt.plot(new_coord[0],new_coord[1],'k.')
    lambda_n = nxt

print('lambda_opt1: ',lambda_n)
plt.grid()
plt.savefig('../figs/gd1.png')
x_opt1 = np.array([3*lambda_n,4*(1-lambda_n)])
print('x_opt1: ',x_opt1)

y2 = function2(x)
plt.plot(x,y2)

alpha = 0.01
lambda_0 =2
eps = 1e-7
count = 0
N = 100000
lambda_n = lambda_0

while count<N and np.abs(alpha*grad2(lambda_n))>eps:
    nxt = lambda_n - alpha*grad2(lambda_n)
    count += 1
    new_coord = np.array([nxt,function2(nxt)])
    curr_coord = np.array([lambda_n,function2(lambda_n)])
    L = line_gen(curr_coord,new_coord)
    plt.plot(L[0],L[1])
    plt.plot(curr_coord[0],curr_coord[1],'k.')
    plt.plot(new_coord[0],new_coord[1],'k.')
    lambda_n = nxt

print('lambda_opt2: ',lambda_n)
plt.grid()
plt.savefig('../figs/gd2.png')
x_opt2 = np.array([3*lambda_n,4*(1-lambda_n)])
print('x_opt2: ',x_opt2)
