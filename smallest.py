smallest=None
array=[12,45,12,78,19,3,56]

for i in array:
    if smallest is  None:
        smallest=i
    elif i<smallest:
        smallest=i

print("The smallest value from",array,"is",smallest)