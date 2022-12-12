#LAGRANGE'S METHOD
#Name - Anmol Dobhal
#Roll No. - 2130139

import numpy as np
import math as mp
n=int(input("enter the no. of data points:"))
x=np.zeros((n))
y=np.zeros((n))
for i in range(n):
    x[i]=float(input("enter the value x["+str(i)+"]="))
    y[i]=float(input("enter the value y["+str(i)+"]="))

a=float(input("enter the value on which formula should be applied:"))
term=0

for i in range(0,n):
    ut=1
    lt=1
    for j in range(n):
        ut=ut*(a-x[j])
        if i!=j:
            lt=lt*(x[i]-x[j])
    term=(ut*y[i])/(lt*(a-x[i]))+term
print(term)


'''enter the no. of data points:5
enter the value x[0]=0
enter the value y[0]=1
enter the value x[1]=1
enter the value y[1]=3
enter the value x[2]=3
enter the value y[2]=49
enter the value x[3]=4
enter the value y[3]=129
enter the value x[4]=7
enter the value y[4]=813
enter the value on which formula should be applied:0.3
1.831'''


