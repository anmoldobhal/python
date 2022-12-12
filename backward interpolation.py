# BACKWARD DIFFERENCE INTERPOLATION
#Name- Anmol Dobhal
#Roll No. - 2130139


import numpy as np
n=int(input("enter the value of data point ="))
x=np.zeros(n)
y=np.zeros((n,n))

for i in range(n):
    x[i]=int(input("enter the value x["+str(i)+"]="))
    y[i][0]=int(input("enter the value y["+str(i)+"]="))

for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i]=y[j][i-1]-y[j-1][i-1]

print("x",end='\t')
print("y",end='\t')
for i in range(1,n):
    print("d"+ str(i)+"y",end='\t')
print("\n")
for i in range(0,n):
    print(x[i],end='\t')
    for j in range(0,i+1):
        print(y[i][j],end='\t')
    print("\n")

term = 1
sum = 0

a=float(input("enter the value where intepolation formula should be applied="))
h=x[2]-x[1]
p=(a-x[n-1])/h

for i in range(n):
    sum=sum+term*y[n-1][i]
    term=(term*(p+i))/(i+1)
print(sum)

#OUTPUT

enter the value of data point =3
enter the value x[0]=1
enter the value y[0]=2
enter the value x[1]=3
enter the value y[1]=4
enter the value x[2]=5
enter the value y[2]=6
x	y	d1y	d2y	

1.0	2.0	

3.0	4.0	2.0	

5.0	6.0	2.0	0.0	

enter the value where intepolation formula should be applied=3
4.0

