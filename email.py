handle=open('mbox-short.txt')

for line in handle:
    line=line.rstrip()
    words=line.split()
    #Gurdian Pattern 
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
