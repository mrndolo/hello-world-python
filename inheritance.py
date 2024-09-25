#inheritance is a mechanism for reusing code
#useful for DRY(don't repeat yourself)
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("barking...")
    pass


class Cat(Mammal):
    def mieow(self):
        print("mieowing...")
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.mieow()