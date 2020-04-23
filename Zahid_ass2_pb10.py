import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


'''
Variable transformation being used here is t=z/(1+z)
thus dx/dz=1/(x^(2)*(1+z)^(2)+z^2) with boundary condition
0<=z<=infinity
'''
h = float(input("enter the step size=", ))
def func(z,x): return 1/(x**(2)*(1-z)**(2)+z**2)



z=np.arange(0,1+h,h)
n=len(z)

x = np.zeros(n)

x[0]=1

for i in range(n-1):
          k0 = h*func(z[i],x[i])
          k1 = h*func(z[i]+h/2,x[i]+k0/2)
          k2 = h*func(z[i]+h/2,x[i]+k1/2)
          k3 = h*func(z[i]+h,x[i]+k2)
          x[i+1]=x[i]+(k0+2*k1+2*k2+k3)/6

    
plt.plot(z,x,"-b")
plt.xlabel("$z$",fontsize=20)
plt.ylabel("x(z)",fontsize=20)
plt.show()

t=(3.5e06)/(3.5e06+1)

f = interpolate.interp1d(z, x)
print("solution(3.5e+06)=",f(t))       
          
