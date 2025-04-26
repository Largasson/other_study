class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return 'мяу'

class Dog(Animal):
    def sound(self):
        return 'гав'

class CatDog(Cat, Dog):
    def sound(self):
        return super().sound()


catdog = CatDog()

print(catdog.sound())