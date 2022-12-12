#Name=Anmol Dobhal
#Roll No.= 2130139
#SIMPSON'S 1/3 RULE


import numpy as np
def fun(x):
    y1=x*x   #any given func
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
    if i%2==0:
        s+=2*(y[i])
    else:
        s+=4*(y[i])
val=(s*h)/3
print("value by integration is:",val)

#Output

'''enter lower limit:1
enter upper limit:10
enter number of intervals:10
value by integration is: 303.0'''

