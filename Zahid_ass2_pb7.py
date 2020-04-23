import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
########################(FIRST EQUATION)####################################################
def solution(t):return ((t/5)*np.exp(3*t)-(1/25)*np.exp(3*t)+(1/25)*np.exp(-2*t))

h=float(input('enter the step size=', ))
y0=0
trange = np.arange(0,1+h,h)
n=len(trange)        
def func(t, y ):return t*np.exp(3*t)-2*y
sol = solve_ivp(func, [trange[0],trange[n-1]], [y0], t_eval=trange)
m=sol.y[0,:]
#print('m=',m)
x = sol.t
plt.plot(sol.t,m,"*k",label="From numpy.solve_ivp")
plt.plot(x, solution(x), label = "From symbolic calculator")
plt.xlabel("t",fontsize=20)
plt.ylabel("y",fontsize=20)
plt.legend()
plt.show()        

####################(SECOND EQUATION)#####################################################################################################

def solution(t):return (t**2 - 3*t + 1)/(t-3)

y0=1
trange = np.arange(2,3+h,h)
n=len(trange)        
def func(t, y ):return 1-(t-y)**2
sol = solve_ivp(func, [trange[0],trange[n-1]], [y0], t_eval=trange)
m=sol.y[0,:]
#print('m=',m)
x = sol.t
plt.plot(sol.t,m,"*k",label="From numpy.solve_ivp")
plt.plot(x, solution(x), label = "From symbolic calculator")
plt.xlabel("t",fontsize=20)
plt.ylabel("y",fontsize=20)
plt.legend()
plt.show()
#####################(THIRD EQUATION)###########################################################################3

def solution(t):return t*np.log(t)+2*t

y0=2
trange = np.arange(1,2+h,h)
n=len(trange)      
def func(t, y ):return (1+y/t)
sol = solve_ivp(func, [trange[0],trange[n-1]], [y0], t_eval= trange)
m=sol.y[0,:]
#print('m=',m)
x = sol.t
plt.plot(sol.t,m,"*k",label="From numpy.solve_ivp")
plt.plot(x, solution(x), label = "From symbolic calculator")
plt.xlabel("t",fontsize=20)
plt.ylabel("y",fontsize=20)
plt.legend()
plt.show()
#######################(FOURTH EQUATION)##################################################################

def solution(t):return (3*np.sin(2*t)-2*np.cos(3*t)+8)/6

y0=1
trange = np.arange(0,1+h,h)
n=len(trange)         
def func(t, y ):return np.cos(2*t)+np.sin(3*t)
sol = solve_ivp(func, [trange[0],trange[n-1]], [y0], t_eval=trange)
m=sol.y[0,:]
#print('m=',m)
x = sol.t
plt.plot(sol.t,m,"*k",label="From numpy.solve_ivp")
plt.plot(x, solution(x), label = "From symbolic calculator")
plt.xlabel("t",fontsize=20)
plt.ylabel("y",fontsize=20)
plt.legend()
plt.show()



























