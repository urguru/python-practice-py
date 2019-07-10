filename=input("Enter the file that you want to read")
handler=open(filename)
count=0
for line in handler:
    line=line.rstrip()
    print(line)
    count+=1
    print('Line Count :',count)

print("Done Printing")

