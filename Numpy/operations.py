import numpy as np

arr1=np.arange(1,11,1).reshape(2,5)
print(arr1)

arr2 = np.arange(11, 21, 1).reshape(2, 5)
print(arr2)

add=arr1+arr2
sub=arr2-arr1
mult=arr1*arr2
div=arr2/arr1
print(add,sub,mult,div,sep='\n')

print(arr1+10)
print(arr1-1)
print(arr1**2)
print(arr1>5)

a1=np.array([[1,1],[1,1]])
a2=np.array([[2,2],[2,2]])
print(a1.dot(a2))
print(a2.dot(a1))
