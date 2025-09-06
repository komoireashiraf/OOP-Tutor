class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof! Whoof!")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("Mathew", "Bombo Rd", "0743820094")
dog1 = Dog("Buddy", "Golden Retriever", owner1)
print(dog1.owner.name)

owner2 = Owner("Marvin", "Bishop Tucker Rd", "0701234567")
dog2 = Dog("Max", "German Shepherd", owner2)
print(dog2.owner.name)
