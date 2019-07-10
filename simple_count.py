counts={}
names=['Apple','Ball','Cat','Dog','Cat','Apple','Cat','Cat','Cat','Dog']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)