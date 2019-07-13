import re
file_name='mbox-short.txt'
handle=open(file_name)
numbers=list()

for line in handle:
    line.rstrip()
    temp=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(temp)!=1: continue
    numbers.append(float(temp[0]))

print(max(numbers))