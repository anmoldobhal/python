#Aim:To solve an Ordinary Differential equation using Rk_2 method.
#Name:Amartya Srivastav
#Roll No:2130203


import numpy as np
import matplotlib.pyplot as plt

n=int(input("Enter the number of points"))
l=float(input("Enter the value of x where you want the value of y"))
x= float(input("Enter the value of x"))
y= float(input("Enter the value of y"))

a=np.zeros((n+1))
b=np.zeros((n+1))

a[0]=x
b[0]=y

def fun(x,y):
    p= (x-y)/2
    return p


h= (l-x)/n

print("The step size =",h)


for i in range(1,n+1):
    a[i]=a[i-1]+h
    k1=h*fun(a[i-1],b[i-1])
    k2=h*fun(a[i-1]+h,b[i-1]+k1)
    b[i]=b[i-1]+(1/2)*(k1+k2)
print(a)
print(b)
print("The value of y is",b[-1])

#plotting

plt.title("The graph of Rk2 method :")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.plot(a,b)
plt.show()
