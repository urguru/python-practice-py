import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
low=np.tril(arr)
high=np.triu(arr)

print(arr)
print(low)
print(high)

arr=np.arange(100).reshape(5,5,4)

print(arr)