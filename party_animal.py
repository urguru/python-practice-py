class partyAnimal:
    x = 0

    def __init__(self):
        print("I'm Constructed")

    def party(self):
        self.x = self.x+1
        print("So far", self.x)

    def __del__(self):
        print("ye Bye")


an = partyAnimal()
an.party()
an.party()

print(dir(partyAnimal))
print(type(an))
