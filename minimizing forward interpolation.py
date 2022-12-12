
#MINIMIZING ERROR BY APPLYING FORWARD INTERPOLATION ANYWHERE
#Name = Anmol Dobhal
#Roll No. - 2130139


#MINIMIZING ERROR BY APPLYING FORWARD INTERPOLATION ANYWHERE


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
for i in range(n):
    if (a<x[i]):
        k=i-1
        break
p=(a-x[k])/h
for i in range(n):
    sum=sum+term*y[k][i]
    term=(term*(p-i))/(i+1)
print(sum)

#Output

'''enter the value of data point =5
enter the value x[0]=2
enter the value y[0]=32
enter the value x[1]=4
enter the value y[1]=33
enter the value x[2]=6
enter the value y[2]=12
enter the value x[3]=8
enter the value y[3]=65
enter the value x[4]=10
enter the value y[4]=4
x	  y	    d1y	  d2y	d3y	   d4y	

2.0	 32.0	1.0	 -22.0	96.0  -284.0	

4.0	 33.0  -21.0  74.0 -188.0	

6.0	 12.0	53.0 -114.0	

8.0	 65.0  -61.0	

10.0 4.0	

enter the value where interpolation formula should be applied:5
1.5

