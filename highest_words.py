file_name=input("Enter the file name : ")
handler=open(file_name)

words=handler.read().split()
count={}

for word in words:
    count[word]=count.get(word,0)+1

bigWord=None
bigCount=None

for word,num in count.items():
    if bigWord==None or num>bigCount:
        bigWord=word
        bigCount=num

print(bigWord,bigCount)