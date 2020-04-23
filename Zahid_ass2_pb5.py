import numpy as np
import matplotlib.pyplot as plt


def f1(x,y):return (-10)


def f2(x,z):return (z)


h=0.001
a=0
b=10
A=40
B=60

z0=np.linspace(A,B,B-A+1)
y0=0
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
z=np.zeros((z0.size,x.size))  

for i in range(len(z0)):
        z1=[]
        z1.append(z0[i])
        for j in range(n):
            ze=z1[j]+f1(x[j],z1[j])*h
            z1.append(ze)
        z[i]=z1
Y=np.zeros((z0.size,x.size))   

for i in range(z0.size):
    y=[]
    y.append(y0)
    for j in range(n):
        ye=y[j]+f2(x[j],z[i][j])*h
        y.append(ye)
    Y[i]=y
    c=0



u=[]               
for i in range(z0.size):
    u.append(abs(Y[i][n]))
c=np.argmin(u,axis=0)


print(c) 
print("z(0) =",z[c][0])

plt.xlabel('x')
plt.ylabel('y')
for k in [x for x in range(7,14) if x != 10]:
    plt.plot(x,Y[k],'--')
plt.plot(x,Y[10],color = 'k',label = 'y vs xtrue')
plt.legend()
plt.show()

