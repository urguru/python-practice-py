counts={}
names=['Apple','Ball','Cat','Dog','Cat','Apple','Cat','Cat','Cat','Dog']
for name in names:
    if name in counts:
        counts[name]=counts[name]+1
    else:
        counts[name]=1

print(counts)
