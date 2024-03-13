#libraries. 1.NUMPY
import numpy as np
arr = np.array([10,20,30,40])
print(arr)
#more than one dimensions
a = np.array([[1,2] , [3,4], [5,6], [7,8]])
print(a)
#minimum dimension
b =np.array([1,2,3,4,5], ndmin =5)
print(b)
#dtype parameter
c =np.array([1,2,3], dtype=complex)
print(c)
d =np.array([1,2,3], dtype=bool)
print(d)
e =np.array([1,2,3,4,5,6], dtype=int)
print(e)

f =np.arange(0,100,5)
f=f.reshape(5,4)
print('Original array is:')
print(f)
t =f.T
print('Transpose \n', t)
print('Modified array is:')
for x in np.nditer(f):
    print(x)