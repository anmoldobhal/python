#AIM- To Run interpolation program
#NAME- Anmol DOBHAL
#ROLL No. - 2130139

#FORRWARD PATH DIFFERNCE


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


'''enter the value of data point =5
enter the value x[0]=1
enter the value y[0]=4
enter the value x[1]=2
enter the value y[1]=77
enter the value x[2]=3
enter the value y[2]=12
enter the value x[3]=4
enter the value y[3]=98
enter the value x[4]=5
enter the value y[4]=22
x	  y	     d1y	d2y	   d3y	   d4y	

1.0	 4.0	 73.0  -138.0  289.0   -602.0	

2.0	 77.0	-65.0	151.0  -313.0	

3.0	 12.0	 86.0  -162.0	

4.0	 98.0	-76.0	

5.0	 22.0	'''












