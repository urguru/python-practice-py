file_name=input("Enter the name of the file that ypu want us to read")
try:
    handler=open(file_name)

except:
    print("Invalid file")
    quit()

words=handler.read().strip().split()

counter=dict()
for word in words:
    counter[word]=counter.get(word,0)+1

top10=list()
for key,value in counter.items():
    newtup=(value,key)
    top10.append(newtup)

top10=sorted(top10,reverse=True)

for key,value in top10[0:10]:
    print(key,value)

print("Done")