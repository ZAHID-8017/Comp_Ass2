import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
########################(FIRST EQUATION)####################################################
h = float(input("enter the step size=", ))
x = np.arange(1,2+h,h)
n = len(x)
def solution(t): return np.log(t)

def func(t,y): return np.vstack((y[1], -np.exp(-2*y[0])))

def bc(ya,yb): return np.array([ya[0],yb[0]-np.log(2)])

y = np.zeros((2,n))

y[0,0]=0

y[0,n-1] = np.log(2)

sol=solve_bvp(func,bc,x,y)


x_plot = np.linspace(1, 2, 100)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,label="From scipy.integrate solve_bvp ")
plt.plot(x_plot,solution(x_plot),"+k",label="Analytic Solution")
plt.title(r'$y=log(t)$')
plt.xlabel("$t$")
plt.ylabel("y(t)")
plt.legend()
plt.show()
          

####################(SECOND EQUATION)#####################################################################################################
x = np.arange(0,0.5*np.pi+h,h)
n = len(x)
def solution(t): return np.exp(np.sin(t))
#here y[1]=dy/dt, y[0]= y
def func(t,y): return np.vstack((y[1], y[1]*np.cos(t)-y[0]*np.log(y[0])))

def bc(ya,yb): return np.array([ya[0]-1,yb[0]-np.exp(1)])

y = np.zeros((2,n))

y[0]=1
sol=solve_bvp(func,bc,x,y)


x_plot = x
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,color="red",label="From scipy.integrate solve_bvp ")
plt.plot(x_plot,solution(x_plot),"g--",label="Analytic Solution")
plt.title(r'$y=np.exp(np.sin(t)$')
plt.xlabel("$t$")
plt.ylabel("y(t)")
plt.legend()
plt.show()
          


#####################(THIRD EQUATION)###########################################################################3

x = np.arange(np.pi/4,np.pi/3+h,h)
n = len(x)
def solution(t): return np.sqrt(np.sin(t))
#here y[1]=dy/dt, y[0]= y
def func(t,y): return np.vstack((y[1], -(2*y[1]**(3)+y[0]**(2)*y[1])/np.cos(t)))

def bc(ya,yb): return np.array([ya[0]-2**(-1/4),yb[0]-(12**(1/4)/2)])

y = np.zeros((2,n))

y[0]=2**(-1/4)
sol=solve_bvp(func,bc,x,y)


x_plot = x
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,color="red",label="From scipy.integrate solve_bvp ")
plt.plot(x_plot,solution(x_plot),"g--",label="Analytic Solution")
plt.title(r'$y=\sqrt{sin(x)}$')
plt.xlabel("$t$")
plt.ylabel("y(t)")
plt.legend()
plt.show()

#######################(FOURTH EQUATION)##################################################################

x = np.arange(0,np.pi+h,h)
n = len(x)
def solution(t): return np.sin(t)+2
#here y[1]=dy/dt, y[0]= y
def func(t,y): return np.vstack((y[1], 1/2-y[1]**(2)/2-y[0]*np.sin(t)/2))

def bc(ya,yb): return np.array([ya[0]-2,yb[0]-2])

y = np.zeros((2,n))

y[0]=2
sol=solve_bvp(func,bc,x,y)


x_plot = x
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,color="red",label="From scipy.integrate solve_bvp ")
plt.plot(x_plot,solution(x_plot),"g--",label="Analytic Solution")
plt.title(r'$y=\sin{x}+2$')
plt.xlabel("$t$")
plt.ylabel("y(t)")
plt.legend()
plt.show()
























