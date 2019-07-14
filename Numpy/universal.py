import numpy as np

arr=np.arange(1,13,1).reshape(4,3)
print(arr)

print(arr.sum())
print(arr.min())
print(arr.max())
print(arr.std())
print(arr.sum(axis=0))
print(arr.min(axis=0))
print(arr.max(axis=0))
print(arr.std(axis=0))
