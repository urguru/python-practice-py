x=list()
while True:
    inp=input(("Enter a number"))
    if inp=='done':
        break
    x.append(int(inp))

print('average is',sum(x)/len(x))