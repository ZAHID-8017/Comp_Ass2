import numpy as np
import matplotlib.pyplot as plt
h = float(input("enter the step size=", ))
n = int(1/h)+1
def f1(u1,u2,u3,t):return(u1+2*u2-2*u3+np.exp(-t))
	
def f2(u1,u2,u3,t):return(u2+u3-2*np.exp(-t))

def f3(u1,u2,u3,t):return(u1+2*u2+np.exp(-t))
t = np.linspace(0,1,n)
#print('t=', t)
u1 = np.zeros(n)
u2 = np.zeros(n)
u3 = np.zeros(n)
u1[0]=3
u2[0]=-1
u3[0]=1
for i in range(0,n-1,1):
	k0=h*f1(u1[i],u2[i],u3[i],t[i])
	l0=h*f2(u1[i],u2[i],u3[i],t[i])
	m0=h*f3(u1[i],u2[i],u3[i],t[i])
	k1=h*f1(u1[i]+h/2,u2[i]+k0/2,u3[i]+l0/2,t[i]+m0/2)
	l1=h*f2(u1[i]+h/2,u2[i]+k0/2,u3[i]+l0/2,t[i]+m0/2)
	m1=h*f3(u1[i]+h/2,u2[i]+k0/2,u3[i]+l0/2,t[i]+m0/2)
	k2=h*f1(u1[i]+h/2,u2[i]+k1/2,u3[i]+l1/2,t[i]+m1/2)
	l2=h*f2(u1[i]+h/2,u2[i]+k1/2,u3[i]+l1/2,t[i]+m1/2)
	m2=h*f3(u1[i]+h/2,u2[i]+k1/2,u3[i]+l1/2,t[i]+m1/2)
	k3=h*f1(u1[i]+h/2,u2[i]+k2,u3[i]+l2,t[i]+m2)
	l3=h*f1(u1[i]+h/2,u2[i]+k2,u3[i]+l2,t[i]+m2)
	m3=h*f1(u1[i]+h/2,u2[i]+k2,u3[i]+l2,t[i]+m2)
	u1[i+1]=u1[i]+(k0+2*k1+2*k2+k3)/6
	u2[i+1]=u2[i]+(l0+2*l1+2*l2+l3)/6
	u3[i+1]=u3[i]+(m0+2*m1+2*m2+m3)/6
	
	
plt.plot(t,u1,".r",label="u1(t)")
plt.plot(t,u2,".g",label="u2(t)")
plt.plot(t,u3,".b",label="u3(t)")
plt.xlabel("$t$",)
plt.legend()
plt.show()
