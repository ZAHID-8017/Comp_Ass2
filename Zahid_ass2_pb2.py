import numpy as np
import matplotlib.pyplot as plt
def dydx(y,x): return (y/x - (y/x)**2)
h=0.1
n=11
t=np.linspace(1,2,n)
w=np.zeros(n,dtype=float)
y_tr = np.zeros(n, dtype = float)
for i in range(n):
    y_tr[i] = t[i]/(1+np.log(t[i]))
w[0]=1
for i  in range(n-1):
    w[i+1] = w[i] + h*dydx(w[i],t[i])
abs_error = np.zeros(n, dtype=float)
rel_error = np.zeros(n, dtype = float)

for i in range(n):
    abs_error[i] = abs(w[i]-y_tr[i])
    rel_error[i] = abs((w[i]-y_tr[i])/w[i])
    


plt.plot(t,w,'r--', label = 'Euler-Backward')
plt.plot(t, y_tr, color = 'blue', label = 'True solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
