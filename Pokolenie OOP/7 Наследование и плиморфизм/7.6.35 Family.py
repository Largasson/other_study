class Family:
    def __init__(self, mood='neutral'):
        self.mood = mood

class Father(Family):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'

class Mother(Family):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass


father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)