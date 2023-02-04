#Aim:To solve an Ordinary Differential equation using modified euler method
#Name:Amartya Srivastav
#Roll No:2130203


import numpy as np
import matplotlib.pyplot as plt

n=int(input("Enter the number of points"))
l=float(input("Enter the value of x where you want the value of y"))
x= float(input("Enter the value of x"))
y= float(input("Enter the value of y"))

a=np.zeros((n+1,1))
b=np.zeros((n+1,1))
c=np.zeros((n+1,1))

def fun (x,y):
    f=(x-y)/2
    return f

h=(l-x)/n

print("The step size=",h)

a[0]=x
b[0]=y
c[0]=y
for i in range(1,n+1):
    a[i]=h+a[i-1]
    b[i]=b[i-1]+(h*fun(a[i-1],b[i-1]))
    c[i]=c[i-1]+(h/2)*(fun(a[i-1],c[i-1])+fun(a[i],b[i]))
print("The final value of y using eulers method",b[n])
if (c[n]-b[n] >= 10^(-3)):
    b=c
    for i in range (1,n+1):
        c[i]=c[i-1]+(h/2)*(fun(a[i-1],c[i-1])+fun(a[i],b[i]))

print("x",end="\t")
print("y")
for i in range(0,n+1):
    print(a[i][0],end="\t")
    print(c[i][0])

print("The final value of y",c[n])
plt.plot(a,c)
plt.show()
