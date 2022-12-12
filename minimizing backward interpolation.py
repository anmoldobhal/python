
#MINIMIZING ERROR BY APPLYING BACKWARD INTERPOLATION ANYWHERE
#Name = Anmol Dobhal
#Roll No.- 2130139


#MINIMIZING ERROR BY APPLYING BACKWARD INTERPOLATION ANYWHERE


import numpy as np
n=int(input("enter the value of data point ="))
x=np.zeros(n)
y=np.zeros((n,n))
term=1
sum=0

for i in range(n):
    x[i]=int(input("enter the value x["+str(i)+"]="))
    y[i][0]=int(input("enter the value y["+str(i)+"]="))

for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i]=y[j][i-1]-y[j-1][i-1]
print("x",end='\t')
print("y",end='\t')

for i in range(1,n):
    print("d"+str(i)+"y",end='\t')
print("\n")

for i in range(0,n):
    print(x[i],end='\t')
    for j in range(0,i+1):
        print(y[i][j],end='\t')
    print("\n")


a=float(input("enter the value where interpolation formula should be applied:"))

h=x[2]-x[1]
for i in range(n):
    if (a<x[i]):
        k=i
        break
p=(a-x[k])/h
for i in range(n):
    sum=sum+term*y[k][i]
    term=(term*(p+i))/(i+1)
print(sum)

#Output

'''enter the value of data point =5
enter the value x[0]=2
enter the value y[0]=21
enter the value x[1]=4
enter the value y[1]=3
enter the value x[2]=6
enter the value y[2]=43
enter the value x[3]=8
enter the value y[3]=6
enter the value x[4]=10
enter the value y[4]=22
x	y	    d1y     d2y	   d3y	  d4y	

2.0	 21.0	

4.0	 3.0   -18.0	

6.0	 43.0   40.0    58.0	

8.0	 6.0    -37.0  -77.0  -135.0	

10.0 22.0	16.0	53.0   130.0  265.0	

enter the value where interpolation formula should be applied:5
11.0625'''

