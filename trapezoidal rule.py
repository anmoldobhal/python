
#NUMERICAL INTEGRATION USING TRAPEZOIDAL RULE


import numpy as np
n=int(input("enter the value of data point ="))
x=np.zeros(n)
y=np.zeros((n,n))
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
h=x[1]-x[0]
s=y[0][0]+y[n-1][0]
for i in range(1,n-1):
    s+=2*y[i][0]
val=(s*h)/2
print("value of integration is=",val)


#Output


'''enter the value of data point =7
enter the value x[0]=-4
enter the value y[0]=0
enter the value x[1]=-3
enter the value y[1]=4
enter the value x[2]=-2
enter the value y[2]=5
enter the value x[3]=-1
enter the value y[3]=3
enter the value x[4]=0
enter the value y[4]=10
enter the value x[5]=1
enter the value y[5]=11
enter the value x[6]=2
enter the value y[6]=2
x	y	d1y	d2y	d3y	d4y	d5y	d6y	

-4.0	0.0	4.0	-3.0	0.0	12.0	-39.0	77.0	

-3.0	4.0	1.0	-3.0	12.0	-27.0	38.0	

-2.0	5.0	-2.0	9.0	-15.0	11.0	

-1.0	3.0	7.0	-6.0	-4.0	

0.0	10.0	1.0	-10.0	

1.0	11.0	-9.0	

2.0	2.0	

value of integration is= 34.0'''

