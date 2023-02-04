#Aim:To solve an Ordinary differential equation by rk4 method.
#Name:Amartya Srivastav 
#Roll No: 2130203
#Date: 3/2/2023

import numpy as np 
import matplotlib.pyplot as plt
n= int(input("Enter the grid number="))
x=float(input("Enter the value of x="))
y=float(input("Enter the value of y= "))
p=float(input("Enter the value of x at which you have to find the value of y= "))

def function(x,y):
    f=(y)
    return f

h=(p-x)/n

a=np.zeros((n+1))
b=np.zeros((n+1))

a[0]=x
b[0]=y
 
for i in range(1,n+1):
    a[i]=a[i-1]+h
    k1=h*function(a[i-1],b[i-1])
    k2=h*function(a[i-1]+h*0.5,b[i-1]+k1*0.5)
    k3=h*function(a[i-1]+h*0.5,b[i-1]+k2*0.5)
    k4=h*function(a[i-1]+h,b[i]+k3)
    b[i]=b[i-1]+(k1+2*k2+2*k3+k4)/6
print("x",end="\t")
print("y")
for i in range(0,n+1):
    print(a[i],end="\t")
    print(b[i],end="\n")
print("The solution of the differential equation using rk4 is",b[n])

#plotting
plt.title("The graph of the given differential equation")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(a,b)
plt.legend(["e^x"],loc="best")
plt.show()
