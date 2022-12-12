# INTERPOLATION PROGRAM FORWARD
#Name = Anmol Dobhal
#Roll No. - 2130139


import numpy as np
n=int(input("enter the value of data point ="))
x=np.zeros(n)
y=np.zeros((n,n))
term=1
sum=0

for i in range(n):
    x[i]=float(input("enter the value x["+str(i)+"]="))
    y[i][0]=float(input("enter the value y["+str(i)+"]="))

for i in range(1,n):
    for j in range(0,n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]

print("x",end='\t')
print("y",end='\t')
for i in range(1,n):
    print("d"+str(i)+"y",end='\t')
print("\n")

for i in range(0,n):
    print(x[i],end='\t')
    for j in range(0,n-i):
        print(y[i][j],end='\t')
    print("\n")

a=float(input("enter the value where interpolation formula should be applied:"))

h=x[2]-x[1]
p=(a-x[0])/h
for i in range(n):
    sum=sum+term*y[0][i]
    term=(term*(p-i))/(i+1)
print(sum)


'''enter the value of data point =5
enter the value x[0]=1
enter the value y[0]=65
enter the value x[1]=2
enter the value y[1]=33
enter the value x[2]=3
enter the value y[2]=11
enter the value x[3]=4
enter the value y[3]=32
enter the value x[4]=5
enter the value y[4]=2
x	 y	    d1y	   d2y	 d3y	d4y	

1.0	 65.0  -32.0   10.0	 33.0  -127.0	

2.0	 33.0  -22.0   43.0	 -94.0	

3.0	 11.0	21.0  -51.0	

4.0	 32.0  -30.0	

5.0	 2.0	

enter the value where interpolation formula should be applied:3
11.0'''

