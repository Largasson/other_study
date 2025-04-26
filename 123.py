<<<<<<< HEAD
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
=======
from collections.abc import Sequence

class TypeSequence(Sequence):
    def __init__(self, values):
        self.values = values
    def __getitem__(self, index):
        value = self.values[index]
        return value, type(value)


data = TypeSequence([10, False, 'beegeek', 3.14])

print(data[1])
>>>>>>> e7bda546a0987df2b393a4460bf6d2f2a19d522b
