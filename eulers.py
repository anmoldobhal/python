#NAME : AMARTYA SRIVASTAV 
#ROLL NO: 2130203
#AIM: To solve an ordinary differential equations using eulers method.
#DATE : 14/01/2023
  
import numpy as np 
import matplotlib.pyplot as plt
n= int(input("Enter the grid number="))
x=float(input("Enter the value of x="))
y=float(input("Enter the value of y="))
p=float(input("Enter the value of x at which you have to find the value of y= "))

def function(x,y):
    f=(y)
    return f

h=(p-x)/n

a=np.zeros((n+1,1))
b=np.zeros((n+1,1))

a[0][0]=x
b[0][0]=y

for i in range (1,n+1):  
    a[i]=h+a[i-1]
for i in range(1,n+1):
    b[i]=b[i-1]+(h*function(a[i-1],b[i-1]))
print("x",end="\t")
print("Y")
for i in range(0,n+1):
    print(a[i][0],end="\t")
    print(b[i][0],end="\n")
print("The value of given differential equation is",b[n])
plt.plot(a,b)
plt.show()

