import numpy as np
x1=np.random.randint(105,size=16)
#print(x1)
x2=np.random.randint(40,size=(3,4))
#print(x2)
x3=np.random.randint(25,size=(3,4,5))
#print(x3)
'''print("dtype:",x3.dtype)

print("x3 ndim:",x3.ndim)

print("x3.shape:",x3.shape)

print("x3.size",x3.size)
#19-08-2023
print(x1)

print(x1[0])
print(x1[-1]
print(x1[-1])
print(x2[1,0])
x1[0]=7.85554 #this will be truncated
print(x1)
print(type(x1))'''

'''x=np.arange(10) #range of array from 0 to n-1 will be created
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::2])
print(x[1::2])'''

'''#the following code is summa
import array as arr
a=arr.array('i',(1,2,3,4,5))
f=np.array(a)
print(type(a))
print(type(f))'''

#Multidimensional subarrays
print(x2)

print(x2[:2, :3]) #2 rows and 3 columns

print(x2[ :3 , ::2]) #all rows, every other column