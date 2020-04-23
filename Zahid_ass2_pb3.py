import numpy as np
import matplotlib.pyplot as plt
#here f represents dy/dx = z
def f(x,y,z):
  return z
#  here dz/dx = y''[x]
def g(x,y,z):
  return (x*np.exp(x)-x-y+2*z)
#print(f(1,2,3))
#print(g(1,4,5))
h = float(input('give step size of the problem=',  ))
x = np.arange(0,1+h,h)
#print(x)
n = int(1/h)+1
print(n)
print(int(1/h))
y = np.zeros(n)
z=np.zeros(n)
#print(y,z)
for i in range(n-1):
  k0=h*f(x[i],y[i],z[i])
  l0=h*g(x[i],y[i],z[i])
  k1=h*f(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
  l1=h*g(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
  k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
  l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
  k3=h*f(x[i]+h,y[i]+k2,z[i]+l2)
  l3=h*g(x[i]+h,y[i]+k2,z[i]+l2)
  y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
  z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6

plt.plot(x,y,color='blue', label='RK')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$\frac{d^2y}{dx^2}+2\frac{dy}{dx}+y = xe^x-x$')
plt.legend()
plt.show()
    	










































 



  


