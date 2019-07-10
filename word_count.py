file_name=input('Enter the file name')
handler=open(file_name)
all_words=handler.read().strip().split()

count={}
for word in all_words:
    count[word]=count.get(word,0)+1

for key in count:
    print(key,count[key])
