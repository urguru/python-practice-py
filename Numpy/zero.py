import numpy as np

arr=np.zeros((2,3,4),dtype='int32')
print(arr)
for i in arr:
    print (i)

arr = np.ones((3, 4), dtype='int32')
print(arr)
for i in arr:
    print(i)

arr = np.empty((3, 4), dtype='int32')
print(arr)
for i in arr:
    print(i)

arr=np.eye(6)

print(arr)

print(np.diag(arr))