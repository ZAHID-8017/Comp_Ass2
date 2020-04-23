import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
h=float(input("enter the step size=", ))
n=int(1/h)+1
################(FIRST PROBLEM)##########################################
x=np.linspace(0,1,n)
y=np.zeros(n)
y[0]=1/3
for i in range(n-1):
    y[i+1] = y[i]/(1+9*h)

plt.plot(x,y ,"+k",color="red",label ="Euler-Backward")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
#################(SECOND PROBLEM)##################################################
def func(y):return(y-h*( - 20*(y-t)**2 + 2*t )-p)

def fprime(w):
	der=1.0+h*40*(w-t)
	return der

for i in range(0,n-1,1):
	t=x[i]
	p=y[i]
	sol = optimize.root_scalar(func, x0=y[i] ,fprime=fprime, method='newton')
	
	y[i+1]=sol.root



ym=func(x)
plt.plot(x,y,color="blue")
plt.xlabel("$x$")
plt.ylabel("y(x)")
plt.show()
