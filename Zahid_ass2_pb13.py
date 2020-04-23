import numpy as np
import matplotlib.pyplot as plt

def solution(t):return 7*t/4+(t**(3)/2)*np.log(t)-(3/4)*t**3

#here y1=dy/dt
def func(y1,y,t): return (1/t**2)*(t**(3)*np.log(t)-2*y+2*t*y1)
#step size
h=0.001
t=np.arange(1,2+h,h)
n=len(t)
y=np.zeros(n)
y[0]=1
y1=np.zeros(n)
y1[0]=0
for i in range(n-1):
    y1[i+1]=y1[i]+h*func(y1[i],y[i],t[i])
    y[i+1]=y[i]+h*y1[i]

plt.plot(t,y,color="green",label="Numerical solution")    
plt.plot(t,solution(t),"r--",label="Analytic solution")
plt.title(r'$y(t)=7t/4+(t**{3}/2)*log(t)-(3/4)*t**(3)$')
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.legend()
plt.show()
