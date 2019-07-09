str=input('Enter a number :')
try:
    istr=int(str)
except:
    istr=-1

if istr!=-1:
    print("Nice work")
else:
    print("You didnt enter a number")

