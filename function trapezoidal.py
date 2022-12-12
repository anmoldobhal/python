#Anmol Dobhal
#Roll No. = 2130139
#TRAPEZOIDAL RULE BY GIVEN FUNCTION

import numpy as np
def fun(x):
    y1=x*x    #this func will be given to us
    return y1
a=int(input("enter lower limit:"))
b=int(input("enter upper limit:"))
n=int(input("enter number of intervals:"))
h=(b-a)/(n-1)

x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    x[i]=a+i*h
    y[i]=fun(x[i])

s=y[0]+y[n-1]
for i in range(1,n-1):
    s+=2*(y[i])
print(s)
val=(s*h)/2
print("value by integration is:",val)


'''enter lower limit:1
enter upper limit:10
enter number of intervals:10
669.0
value by integration is: 334.5'''

