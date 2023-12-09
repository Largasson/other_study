class Pet:
    lst = []
    def __init__(self, name):
        self.name = name
        Pet.lst.append(self)

    @classmethod
    def first_pet(cls):
        return cls.lst[0] if len(cls.lst) > 0 else None

    @classmethod
    def last_pet(cls):
        return cls.lst[-1] if len(cls.lst) > 0 else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.lst)


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())